"""
Extract step of the ETL pipeline.

Fetches data from an API and returns a cleaned batch
of records based on required fields.
"""

import requests, csv, os
from config import API_URL, BATCH_SIZE

def get_data(start):
    """
    Fetch and clean a batch of data from the API.

    Args:
        start (int): starting index for batch

    Returns:
        list: cleaned records
    """
    url = API_URL
    batch_size = int(os.getenv("BATCH_SIZE", BATCH_SIZE))
    end = start + batch_size
    
    try:
        r = requests.get(url)
        data = r.json()
        print("Fetching data...")
    except Exception as e:
        print("Error fetching data:", e)
        return []
    
    cleaned_data = []

    # process only the required slice (batch)
    for item in data[start:end]:

        # skip records missing required fields
        if "userId" not in item or "id" not in item or "title" not in item:
            continue
        
        clean = {
            "userId": item["userId"],
            "id": item["id"],
            "title": item["title"]
        }
        
        cleaned_data.append(clean)

    print(f"Prepared {len(cleaned_data)} records")
    return cleaned_data