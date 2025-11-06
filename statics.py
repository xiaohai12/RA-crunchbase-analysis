
VC_FUND_TYPES = [
    'seed', 'series_unknown', 'series_a', 'pre_seed', 'series_b', 'angel',
    'series_c', 'convertible_note', 'corporate_round', 'undisclosed',
    'series_d', 'series_e', 'series_f', 'series_g', 'series_h', 'series_i', 'series_j'
]




platform_categories = [
    # Core marketplaces and sharing
    'Marketplace', 'E-Commerce', 'E-Commerce Platforms', 'Online Auctions',
    'Auctions',  'Crowdfunding', 'Funding Platform',
    'Peer to Peer', 'Sharing Economy', 'Collaborative Consumption',
    'Classifieds', 'Rental', 'Group Buying', 'Ride Sharing',
    'Car Sharing', 'Food Delivery', 'Delivery Service', 'Ticketing',
    'Price Comparison', 'Trading Platform', 'Financial Exchanges',

    # Social & communication platforms
    'Social Media', 'Social Network', 'Communities',  'Messaging',
    'Social Bookmarking', 'Private Social Networking',
    'Professional Networking', 'Social Recruiting', 'Online Forums',
    'Social Shopping', 'Social News', 
    'Dating', 

    # Content / creator platforms
    'Video Streaming', 'Music Streaming',  'Video on Demand',
    'Video Sharing', 'Photo Sharing', 'Blogging Platforms', 'Streaming',

    # Financial / fintech platforms
    'Payments', 'Mobile Payments', 
    'Trading Platform', 'Financial Exchanges',

    # Developer & SaaS ecosystems
    'Developer Platform', 'App Discovery', 
    'App Store', 'PaaS', 'Cloud Platform', 

    # Other multi-sided / intermediation cases
    'Crowdsourcing', 'Job Marketplace', 'Recruiting Platform',
    'Online Education Platform', 'Freelance',
    'Funding Platform', 
]

non_platform_categories = [
    # --- Industrial / Manufacturing / Engineering ---
    "Manufacturing", "Industrial", "Industrial Engineering", "Industrial Design",
    "Industrial Automation", "Machinery Manufacturing", "Mechanical Design",
    "Mechanical Engineering", "Electrical Distribution", "Aerospace", "Automotive",
    "Construction", "Building Material", "Facility Management", "Hardware",
    "Computer Hardware", "Electronics", "Semiconductor", "3D Printing", "Robotics",
    "Embedded Systems", "Embedded Software", "Sensor", "Laser", "Optical Communication",
    "Chemical", "Advanced Materials", "Metals", "Mining", "Oil and Gas", "Energy",
    "Renewable Energy", "Solar", "Wind Energy", "Nuclear", "Power Grid", "Utilities",
    "Smart Building", "Green Building", "Heating  Ventilation  and Air Conditioning (HVAC)",

    # --- Healthcare / Biotech / Pharma / Life Science ---
    "Health Care", "Healthcare Services", "Medical", "Medical Device", "Medical Equipment",
    "Pharmaceutical", "Biotechnology", "Biotech", "Life Science", "Health Diagnostics",
    "Clinical Trials", "Genetics", "Therapeutics", "Precision Medicine", "Hospital",
    "Nursing and Residential Care", "Primary and Urgent Care", "mHealth", "Telehealth",
    "MedTech", "Rehabilitation", "Fertility", "Dental", "Wellness", "Personal Health",
    "Health Insurance", "HealthTech",

    # --- Finance (Traditional / Non-platform) ---
    "Banking", "Insurance", "Wealth Management", "Asset Management", "Private Equity",
    "Venture Capital", "Investment Banking", "Hedge Funds", "Mutual Funds", "Pension",
    "Finance", "Accounting", "Bookkeeping and Payroll", "Credit Bureau", "Credit Cards",
    "Commercial Lending", "Consumer Lending", "Financial Consulting", "Financial Planning",
    "Tax Consulting", "Tax Preparation", "Compliance", "Risk Management", "Audit",

    # --- Professional Services / Consulting / Agencies ---
    "Consulting", "Management Consulting", "IT Consulting", "Business Consulting",
    "Strategy Consulting", "Professional Services", "Legal", "Law", "Legal Tech",
    "Accounting", "Auditing", "Recruiting", "Staffing Agency", "HR Consulting",
    "Corporate Training", "Career Planning", "Coaching", "Outsourcing", "Advisory",
    "Agency", "Creative Agency", "Design Agency", "Marketing Agency", "Advertising Agency",
    "Public Relations", "Digital Marketing", "SEO", "SEM", "Direct Marketing",
    "Brand Marketing",

    # --- Education / Research / Non-Profit ---
    "Education", "EdTech", "E-Learning", "Universities", "Primary Education",
    "Secondary Education", "Vocational Education", "Continuing Education", "Higher Education",
    "Research", "Laboratory", "Institute", "Non Profit", "Charity", "Humanitarian",
    "CivicTech", "Government", "GovTech", "Politics", "Advocacy", "Think Tank",
    "Public Safety", "Homeland Security",

    # --- Real Estate / Construction / Property Services ---
    "Real Estate", "Property Management", "Real Estate Investment", "Property Development",
    "Real Estate Brokerage", "Facilities Support Services", "Facility Management",
    "Architecture", "Interior Design", "Home Renovation", "Home Improvement",
    "Construction Tech", "Civil Engineering", "Smart Building",

    # --- Energy / Agriculture / Environment ---
    "Agriculture", "Farming", "AgTech", "Forestry", "Fisheries", "Aquaculture", "Water",
    "Water Purification", "Waste Management", "Recycling", "GreenTech", "Biofuel",
    "Geothermal Energy", "Fuel Cell", "Pollution Control", "Environmental Consulting",
    "Environmental Engineering", "Sustainability Consulting",

    # --- Retail / Consumer Goods / Food ---
    "Retail", "Wholesale", "Consumer Goods", "Consumer Electronics", "Fashion",
    "Apparel", "Beauty", "Cosmetics", "Food and Beverage", "Restaurants", "Bars",
    "Hospitality", "Hotel", "Travel Agency", "Tour Operator", "Grocery", "Snack Food",
    "Wine And Spirits", "Coffee", "Tea", "Bakery", "Catering", "Packaged Food",
    "Fast-Moving Consumer Goods", "Home Appliances",

    # --- Transportation / Logistics / Supply Chain ---
    "Shipping", "Logistics", "Freight Service", "Warehousing", "Delivery Service",
    "Supply Chain Management", "Fleet Management", "Automotive Manufacturing",
    "Aviation", "Railroad", "Marine Transportation", "Ports and Harbors",
    "Courier Service", "Trucking", "Navigation", "GPS",

    # --- Media / Entertainment (Traditional / Linear) ---
    "Broadcasting", "Media and Entertainment", "Film Production", "TV Production",
    "Radio", "Music Label", "Publishing", "News", "Journalism", "Book Publishing",
    "Magazine", "Advertising", "Creative Content", "Animation", "Video Games",
    "Gaming", "Theatre", "Cinema", "Streaming"
]

# ----------------------------
# 🚀 PLATFORM KEYWORDS
# ----------------------------
platform_keywords = [
    # Core Platform Structure
    "platform", "marketplace", "exchange", "two-sided", "multi-sided",
    "peer-to-peer", "p2p", "ecosystem", "network effects", "intermediary",
    "aggregator", "matchmaking", "api marketplace", "app store",
    "developer platform", "partner platform", "digital platform",
    "cloud platform", "platform-as-a-service", "p2p marketplace",

    # E-Commerce / Retail Platforms
    "e-commerce", "online marketplace", "buy and sell", "seller", "vendor",
    "merchant", "storefront", "shopping platform", "auction", "listings",
    "rental marketplace", "price comparison", "dropshipping", "booking platform",
    "delivery marketplace", "product discovery", "digital commerce",
    "b2c marketplace", "b2b marketplace",

    # Social / Communication / Media Platforms
    "social network", "social media", "social platform", "sharing platform",
    "content creators", "user-generated content", "ugc", 
    "community", "online community",  "social app",
    "discussion forum", "messaging platform", "chat platform",
    "communication platform", "blogging platform", "video sharing",
    "photo sharing", "livestreaming", "streaming platform", "subscription platform",

    # FinTech / Blockchain / Exchange Platforms
    "trading platform", "investment platform", "payment platform",
    "digital wallet", "wallet app", "remittance platform", "crowdfunding",
    "crowdlending", "peer lending", "crypto exchange", "cryptocurrency platform",
    "token marketplace", "defi", "nft marketplace", "blockchain network",
    "financial marketplace", "robo-advisor", "brokerage platform",
    "wealth platform", "asset exchange", "loan marketplace",
    "peer-to-peer lending", "payment gateway", "online broker",
    "stock trading", "derivatives exchange",

    # On-demand / Gig Economy / Mobility
    "ride-hailing", "ride sharing", "car sharing", "bike sharing",
    "mobility platform", "delivery app", "delivery platform", "on-demand services",
    "driver and rider", "food delivery platform", "courier platform",
    "gig economy", "freelance marketplace", "service marketplace",
    "home services platform",

    # SaaS / Developer / Enterprise Ecosystem
    "saas marketplace", "integration platform", "api hub", "developer ecosystem",
    "partner ecosystem", "extension marketplace", "plugin marketplace",
    "app integration", "data marketplace", "cloud marketplace",
    "software marketplace", "analytics platform", "platform services",
    "digital ecosystem", "dev platform", "no-code platform", "low-code platform",

    # Education / Crowdsourcing / Knowledge
    "learning platform", "education platform", "mooc", "course marketplace",
    "student and teacher", "tutoring platform", "knowledge sharing",
    "crowdsourcing", "crowd collaboration", "freelance platform",
    "talent marketplace", "expert marketplace", "online classes",

    # Ads / Media / Content Monetization
    "ad network", "ad exchange", "demand side platform", "supply side platform",
    "programmatic", "advertising exchange", "publisher network", "creator economy",
    "media marketplace", "content distribution", "content monetization",

    # Real Estate / Travel / Ticketing Platforms
    "property marketplace", "rental platform", "vacation rental", "travel platform",
    "booking platform", "accommodation marketplace", "real estate marketplace",
    "housing platform", "hotel booking", "ticketing platform", "event platform",
    "reservation system",

    # Generic Platform Synonyms
    "connects users", "connects buyers and sellers", "facilitates transactions",
    "connects businesses and customers", "connects people",
    "intermediates between", "digital hub", "matchmaker",
    "aggregates supply and demand", "two-sided market",
    "multi-party ecosystem", "connectivity", "network-based",
    "ecosystem participants"
]


# ----------------------------
# 🧱 NON-PLATFORM KEYWORDS
# ----------------------------
non_platform_keywords = [
    # Linear Production / Industry
    "manufacturing", "production", "factory", "supply chain", "equipment",
    "hardware", "plant", "assembly", "processing", "wholesale", "distribution",
    "industrial", "engineering", "construction", "infrastructure", "supplier", "photo editor", "photo editing", "creator tools", "content marketing", "video editor", "video editing",

    # Professional / Consulting / Services
    "consulting", "agency", "advisory", "outsourcing", "professional services",
    "training", "education provider", "management consulting", "law firm",
    "legal services", "accounting", "auditing", "human resources",
    "recruitment agency", "research firm", "laboratory", "testing services", "marketing agency",

    # Finance (Traditional)
    "investment firm", "venture capital", "private equity", "fund management",
    "asset management", "banking", "insurance", "pension", "wealth management",
    "financial advisor", "broker dealer", "mortgage provider",

    # Healthcare / Biotech / Science
    "pharmaceutical", "biotech", "medical device", "healthcare", "hospital",
    "clinic", "therapeutics", "life sciences", "diagnostics", "drug development",
    "biotechnology", "medtech",

    # Real Assets / Energy
    "energy", "mining", "oil", "gas", "power generation", "solar farm",
    "wind farm", "utilities", "construction", "real estate development",
    "property management", "architecture",

    # Retail / Consumer Goods
    "retail", "consumer goods", "food manufacturing", "restaurant", "hotel",
    "travel agency", "hospitality", "wholesale", "product line", "distribution",
    "packaged goods", "fashion brand", "cosmetics brand", "hardware store"
]