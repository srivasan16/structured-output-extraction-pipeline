import pymupdf

def extract_pdf_text(pdf_path):
    document = pymupdf.open(pdf_path)
    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    return text


if __name__ == "__main__":
    pdf = "data/input/sample_offer_letter.pdf"

    text = extract_pdf_text(pdf)

    print("=" * 60)
    print(text)
    print("=" * 60)