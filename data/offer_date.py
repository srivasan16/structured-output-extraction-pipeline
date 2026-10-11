def normalize_offer_date(json_data):
    if "date" in json_data:
        json_data["offer_date"] = json_data.pop("date")

    if "document_type" not in json_data:
        json_data["document_type"] = "OFFER LETTER"

    return json_data