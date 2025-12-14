from google import genai
from google.genai import types
import json 
from tqdm import tqdm
import pandas as pd
from google.cloud import storage
from google.oauth2 import service_account
import mimetypes
import time
from typing import List, Tuple, Dict, Any
import re
import logging
logging.basicConfig(level=logging.INFO)



# API_KEY = ???? 


# new SDK clients
# client = genai.Client(api_key=API_KEY)
# batch_client = genai.BatchesClient(api_key=API_KEY)
# models_client = genai.ModelsClient(api_key=API_KEY)

# bucket_name = "ra-crunchbase"
# blob_name = "crunchbase_batch/batch_input.jsonl"
# MODEL_NAME = "models/gemini-2.5-flash-lite"


def build_prompt(meta):
    return f"""
    You are an expert in business models and platform economics.

    Your task: classify a company as 
    - PLATFORM (multi-sided, marketplace, network orchestrator)
    - NON-PLATFORM (linear business)
    - UNCERTAIN (insufficient information)

    Platform = facilitates interactions between two or more distinct user groups
    (Examples: marketplace, gig platforms, app store, booking platforms, b2b2c networks, e-commerce, financial services platform, messenger services)

    Company metadata:
    =================
    UUID: {meta.get('uuid')}
    Name: {meta.get('name')}
    Description: {meta.get('description')}
    Categories: {meta.get('category_list')}
    Category_groups: {meta.get('category_groups_list')}
    Short Description: {meta.get('short_description')}
    Homepage: {meta.get('homepage_url')}
    Country: {meta.get('country_code')}
    =================

    Return a JSON ONLY with:
    {{
    "uuid": "the company's UUID",
    "name": "the company's Name",
    "classification": "platform | non-platform | uncertain",
    "confidence": 0-100,
    "reason": "short explanation"
    }}
    """


# def classify_company(meta):
#     prompt = build_prompt(meta)
#     response = model.generate_content(prompt)
    
#     text = response.text.strip()
#     text = text.replace("```json","").replace("```","")
    
#     try:
#         return json.loads(text)
#     except:
#         return {"uuid": meta['uuid'],"classification": "uncertain", "confidence": 0, "reason": "Parsing error"}
    

# # method 1 

# def process_companies(org_df):
#     results = []
#     for _, row in tqdm(org_df.iterrows(), total=len(org_df)):
#         meta = row.to_dict()
#         out = classify_company(meta)
#         out['uuid'] = row['uuid']  # 加入公司ID，方便合并
#         results.append(out)
#     df_result = pd.DataFrame(results)
#     df_result.to_csv("crunchbase_classification_results_sample.csv", index=False)
#     return pd.DataFrame(results)





def estimate_avg_tokens(org_df: pd.DataFrame, client, n: int = 100) -> float:
    """Estimates the average token count of the prompt using a sample."""
    toks = []
    # Use .sample(min(n, len(org_df))) for safety
    sample_size = min(n, len(org_df))
    for sample in org_df.sample(sample_size).to_dict("records"):
        p = build_prompt(sample)
        # Note: count_tokens returns a token count, no need to catch exception for estimate
        r = client.models.count_tokens(
            model="models/gemini-2.5-flash-lite",
            contents=p
        )
        toks.append(r.total_tokens)
    return sum(toks) / len(toks)

def split_into_token_safe_batches(org_df: pd.DataFrame, avg_tokens: float, max_tokens: int = 4000):
    """Splits the dataframe into batches, estimating safety by token count."""
    batches = []
    current_batch = []
    current_tokens = 0

    for _, row in tqdm(org_df.iterrows(), total=len(org_df), desc="Creating Batches"):
        meta = row.to_dict()
        prompt = build_prompt(meta)

        # We check if adding the *next* average prompt size will exceed the limit.
        if current_tokens + avg_tokens > max_tokens and current_batch:
            # Store the current batch, then reset
            batches.append(current_batch)
            current_batch = []
            current_tokens = 0

        # Add the current item to the new or ongoing batch
        current_batch.append((row["uuid"], prompt))
        current_tokens += avg_tokens # Increment by the average size

    if current_batch:
        batches.append(current_batch)

    return batches

def write_jsonl_batches(batches: List[List[Tuple[str, str]]], prefix: str = "batch_part") -> List[str]:
    """
    Writes all token-safe batches into individual JSONL files using the 
    correct structure for the Gemini Batch API: {"key": "...", "request": {...}}.
    """
    filenames = []
    
    # 💡 IMPORTANT: Note the change in structure below!
    for i, batch in enumerate(batches):
        filename = f"{prefix}_{i}.jsonl"
        with open(filename, "w", encoding="utf-8") as f:
            for uuid, prompt in batch:
                # This structure aligns with the Batch API's requirement:
                line = {
                    # 1. 'key' field is required for tracking the result
                    "key": uuid, 
                    # 2. 'request' field contains the GenerateContentRequest payload
                    "request": {
                        # 3. The contents array contains the prompt parts
                        "contents": [
                            {
                                "role": "user",
                                "parts": [
                                    {"text": prompt.strip()}
                                ]
                            }
                        ]
                        # You could add 'config' here if you need max_output_tokens, temperature, etc.
                    }
                }
                f.write(json.dumps(line) + "\n")
        filenames.append(filename)

    logging.info(f"Successfully created {len(filenames)} JSONL files with the correct format.")
    return filenames


def upload_and_run_batch_jobs(files: List[str], client) -> List[Any]:
    """
    Uploads files and starts all batch jobs without waiting for completion.
    Returns a list of all initiated job objects.
    """
    jobs = []
    failed_files = []
    
    # 1. Start all jobs concurrently
    for f in tqdm(files, desc="Starting Batch Jobs"):
        logging.info(f"\n--- Starting Job for {f} ---")
        
        # 1a. Upload to File API (Required for Batch API input)
        try:
            uploaded_file = client.files.upload(
                file=f,
                config=types.UploadFileConfig(display_name=f'batch-input-{f}',
                                              mime_type='application/jsonl')
            )
            logging.info(f"Uploaded {f} to {uploaded_file.name}")
        except Exception as e:
            logging.info(f"⚠️ ERROR uploading {f}: {e}")
            continue

        # 1b. Run Batch Job
        try:
            job = client.batches.create(
                model="models/gemini-2.5-flash-lite",
                src=uploaded_file.name,
                config={
                    'display_name': f"crunchbase-job-{f}",
                },
            )
            logging.info(f"Started job {job.name}. Initial State: {job.state.name}")
            jobs.append(job)
        except Exception as e:
            logging.info(f"⚠️ ERROR starting job for {uploaded_file.name}: {e}")
            failed_files.append(f)
            continue

    return jobs, failed_files

def poll_batch_jobs(jobs: List[Any], client, poll_interval: int = 30) -> Dict[str, Any]:
    """
    Monitors a list of running batch jobs asynchronously until all are complete.
    Returns a dictionary of final job statuses and output files.
    """
    results = {}
    running_jobs = {job.name: job for job in jobs}
    
    logging.info(f"\n--- Monitoring {len(running_jobs)} Batch Jobs ---")
    
    while running_jobs:
        
        # 2. Iterate and check the status of all currently running jobs
        jobs_to_remove = []
        for job_name in list(running_jobs.keys()): # Iterate over a copy of keys
            try:
                job = client.batches.get(name=job_name)
                state = job.state.name
                
                if state in ("JOB_STATE_SUCCEEDED", "JOB_STATE_FAILED", "JOB_STATE_CANCELLED"):
                    # Job is complete, record final status and output file
                    jobs_to_remove.append(job_name)
                    results[job_name] = {
                        "final_state": state,
                        "output_file": job.dest.file_name if job.dest.file_name else None,
                    }
                    logging.info(f"✅ Job {job_name} **{state}**. Output: {job.dest.file_name if job.dest.file_name else 'N/A'}")
                else:
                    # Job is still running
                    logging.info(f"⏳ Job {job_name} is {state}...")
                    running_jobs[job_name] = job # Update the job object

            except Exception as e:
                # Handle API errors during polling (e.g., job no longer exists)
                jobs_to_remove.append(job_name)
                results[job_name] = {"final_state": "POLLING_ERROR", "error": str(e)}
                logging.info(f"⚠️ ERROR polling job {job_name}: {e}")
                
        # Remove completed jobs from the monitoring list
        for job_name in jobs_to_remove:
            if job_name in running_jobs:
                del running_jobs[job_name]

        if running_jobs:
            logging.info(f"\n{len(running_jobs)} jobs remaining. Waiting {poll_interval} seconds...\n")
            time.sleep(poll_interval) # Wait before polling again

    logging.info("\n--- All Batch Jobs Completed ---")
    return results


def extract_output_file_content(client, file_name: str) -> bytes:
    """Downloads the content of the specified output file from the client."""
    file_content_bytes = client.files.download(file=file_name)
    logging.info(f"File downloaded successfully. Size: {len(file_content_bytes)} bytes")
    
    # Decode the bytes to a string
    file_content_str = file_content_bytes.decode('utf-8')
    results_list = []
    
    # 3. Process the JSON Lines string line by line
    for line in file_content_str.splitlines():
        if not line.strip():
            continue
            
        try:
            # The raw line format: {"key": "UUID", "response": {<GenerateContentResponse>}}
            result_obj = json.loads(line)
            uuid = result_obj.get("key") 
            
            # Navigate deep into the response structure to get the model's text
            model_output_text = result_obj.get("response", {}) \
                                            .get("candidates", [{}])[0] \
                                            .get("content", {}) \
                                            .get("parts", [{}])[0] \
                                            .get("text", "")
            
            # Extract and parse the inner JSON containing classification data
            classification_data = extract_classification_data(model_output_text)
            
            if classification_data and classification_data.get("uuid"):
                # We only keep the fields you requested (uuid, classification, confidence, reason)
                results_list.append({
                    "uuid": classification_data.get("uuid"),
                    'name': classification_data.get("name"),
                    "classification": classification_data.get("classification"),
                    "confidence": classification_data.get("confidence"),
                    "reason": classification_data.get("reason")
                })
            else:
                results_list.append({"uuid": uuid, "classification": "uncertain", "confidence": 0, "reason": "Malformed output from model."})
            
        except Exception as e:
            logging.info(f"⚠️ Failed to process line for UUID {uuid}: {e}")

    # Return the processed data as a DataFrame
    return pd.DataFrame(results_list)




def extract_classification_data(text_response: str) -> Dict[str, Any]:
    """
    Robustly extracts and parses the classification JSON object from 
    the model's text (handling markdown fences and surrounding text).
    """
    # 1. Use regex to reliably extract the JSON block (content between the first { and last })
    json_match = re.search(r"\{.*\}", text_response, re.DOTALL)
    
    if json_match:
        json_string = json_match.group(0)
    else:
        # Fallback cleanup (removes common markdown fences)
        json_string = text_response.replace("```json", "").replace("```", "").strip()

    try:
        return json.loads(json_string)
    except json.JSONDecodeError:
        return None # Return None if parsing fails