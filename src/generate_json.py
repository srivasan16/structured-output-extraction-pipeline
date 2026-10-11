import os
import json
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError(
        "GEMINI_API_KEY not found.\n"
        "Please set your Gemini API key in the .env file."
    )

client = genai.Client(api_key=api_key)

MODEL_NAME = "gemini-3.5-flash-lite"

def generate_structured_json(document_text):

    prompt = f"""
You are an AI information extraction system.

Extract information from the document.

Return ONLY valid JSON.

Use EXACTLY these field names:

{{
    "company_name": "",
    "offer_date": "",
    "document_type": "",
    "candidate_name": "",
    "position": "",
    "employee_id": "",
    "department": "",
    "joining_date": "",
    "annual_ctc": "",
    "work_location": "",
    "reporting_manager": "",
    "benefits": []
}}

If any field is missing, use null.

Document:

{document_text}
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    text = response.text.strip()

    # Remove markdown if Gemini accidentally returns it
    text = text.replace("```json", "")
    text = text.replace("```", "")
    text = text.strip()

    try:
        data = json.loads(text)
        return data

    except json.JSONDecodeError as e:
        print("=" * 60)
        print("❌ Gemini returned invalid JSON")
        print("=" * 60)
        print(e)
        print("\nRaw Response:\n")
        print(text)
        return None


if __name__ == "__main__":

    sample_text = """
TECHVISION TECHNOLOGIES PRIVATE LIMITED

Date: 10 October 2026

OFFER LETTER

Dear Arun Kumar,

We are pleased to offer you the position of AI Software Engineer.

Employee ID: TVT1026

Department: Artificial Intelligence

Joining Date: 01 November 2026

Annual CTC: ₹12,00,000

Work Location:
Chennai, Tamil Nadu

Reporting Manager:
Rahul Sharma

Benefits
Health Insurance
Provident Fund
Performance Bonus
"""

    result = generate_structured_json(sample_text)

    print("=" * 60)
    print(json.dumps(result, indent=4, ensure_ascii=False))
    print("=" * 60)