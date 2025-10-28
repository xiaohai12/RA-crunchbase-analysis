# VC Classification & Exit Analysis Using LLMs

This project investigates how venture capital funding dynamics and exit outcomes differ between **platform** and **non-platform** firms. The classification of firms is performed using **Large Language Models (LLMs)** applied to Crunchbase data and company descriptions. The project is part of a research assistantship at **HEC Lausanne (University of Lausanne)**.

## 🔍 Project Overview

- **Objective**: Identify whether platform firms exhibit different VC funding patterns and exit probabilities (e.g. IPO, acquisition) compared to non-platform firms.
- **Key Tasks**:
  - Automatically classify firms as platform or non-platform using LLMs (OpenAI / HuggingFace models)
  - Extract text-based features (e.g., keywords, embeddings, categories) from Crunchbase profiles
  - Merge with structured VC funding and exit data for downstream econometric analysis

## 🧠 Methods & Tools

- **Text Classification(TODO??)**:  
  - GPT-4 (prompt-based classification)  
  - Open-source alternatives (e.g. `sentence-transformers`, `LLMClassifier`, `LangChain` pipelines)  
  - Keyword-augmented rules for weak supervision

- **Data Sources**:  
  - Crunchbase (organization descriptions, categories, investors)  

- **Feature Engineering**:  
  - Firm embedding generation (e.g. `OpenAIEmbeddings`, `Sentence-BERT`)  
  - Keyword extraction & topic clustering  

- **Analysis**:  
  - Exploratory statistics on funding amount, round frequency, time-to-exit  
  - Logistic regression / survival analysis for exit outcomes

## 📁 Repository Structure