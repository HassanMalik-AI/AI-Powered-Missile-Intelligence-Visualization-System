import json
from groq import Groq
import os

def clean_extracted_data(raw_text, filename):
    """Use LLM to structure raw OCR text"""
    
    client = Groq(api_key="gsk_9F3C6x3jFq7jJg3c7fKzWGdyb3FY3c5WJ3p1C3X5J3Fq7jJg3c7fKzWGdyb3FY3c5WJ3p1C3X5")
    
    prompt = f"""
    Here is raw OCR text from a missile image:
    ---
    {raw_text}
    ---
    Extract this information as JSON:
    - system_name: name of the missile
    - country: country of origin
    - type: missile classification
    - range_km: range in kilometers (as number)
    - year_introduced: year (as number)
    - status: Active/Retired/Development
    
    Return ONLY valid JSON.
    """
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return json.loads(response.choices[0].message.content)