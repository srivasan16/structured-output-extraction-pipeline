from src.resume_schema import OfferLetter
from pydantic import ValidationError


def validate_json(data):

    try:
        result = OfferLetter(**data)

        print("=" * 60)
        print("✅ JSON Validation Successful")
        print("=" * 60)

        return result

    except ValidationError as e:

        print("=" * 60)
        print("❌ JSON Validation Failed")
        print("=" * 60)

        print(e)

        return None