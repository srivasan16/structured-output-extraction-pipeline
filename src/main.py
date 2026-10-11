import json

from src.extract_text import extract_pdf_text
from src.generate_json import generate_structured_json
from src.validator import validate_json
from src.save_json import save_json


PDF_FILE = "data/input/sample_offer_letter.pdf"
OUTPUT_FILE = "data/output/output.json"


def main():

    print("=" * 60)
    print("Structured Output Extraction Pipeline")
    print("=" * 60)

    # STEP 1
    print("\nSTEP 1 : Extracting Text from PDF...\n")

    text = extract_pdf_text(PDF_FILE)

    print(text)

    # STEP 2
    print("\n" + "=" * 60)
    print("STEP 2 : Generating Structured JSON using Gemini")
    print("=" * 60)

    json_data = generate_structured_json(text)

    if json_data is None:
        print("❌ Failed to generate JSON.")
        return

    print(json.dumps(json_data, indent=4, ensure_ascii=False))

    # STEP 3
    print("\n" + "=" * 60)
    print("STEP 3 : Validating JSON")
    print("=" * 60)

    try:
        validated_data = validate_json(json_data)

        if validated_data is None:
            print("\n❌ Project stopped because validation failed.")
            return

        print("\n✅ Validation Successful")
    except Exception as e:
        print("❌ Validation Failed")
        print(e)
        return

    # STEP 4
    print("\n" + "=" * 60)
    print("STEP 4 : Saving JSON")
    print("=" * 60)

    save_json(json_data, OUTPUT_FILE)

    print(f"✅ JSON saved successfully.")
    print(f"📂 Location : {OUTPUT_FILE}")

    print("\n" + "=" * 60)
    print("🎉 PROJECT COMPLETED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    main()