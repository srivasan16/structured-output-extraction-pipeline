# 📄 Structured Output Extraction Pipeline

An AI-powered document processing pipeline that extracts text from PDF documents, converts it into structured JSON using the Google Gemini API, validates the extracted data with Pydantic, and saves the final output as a JSON file.

---

## 🚀 Features

- 📄 Extract text from PDF documents
- 🤖 Convert unstructured text into structured JSON using Google Gemini
- ✅ Validate JSON with Pydantic
- 💾 Save validated JSON to disk
- 🛡️ Error handling for invalid JSON
- 🔑 Environment variable support using `.env`

---

## 🛠️ Tech Stack

- Python 3.13+
- Google Gemini API
- PyMuPDF (PDF Text Extraction)
- Pydantic
- python-dotenv
- JSON

---

## 📂 Project Structure

```text
Structured-Output-Extraction-Pipeline/
│
├── data/
│   ├── input/
│   │   └── sample_offer_letter.pdf
│   └── output/
│       └── output.json
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── extract_text.py
│   ├── generate_json.py
│   ├── validator.py
│   ├── resume_schema.py
│   └── save_json.py
│
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
└── LICENSE
```

---

# ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Structured-Output-Extraction-Pipeline.git

cd Structured-Output-Extraction-Pipeline
```

### 2. Create Virtual Environment

Windows

```bash
python -m venv .venv
```

Activate

```bash
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

```text
GEMINI_API_KEY=YOUR_API_KEY
```

---

# ▶️ Run the Project

```bash
python -m src.main
```

---

# 🔄 Pipeline Workflow

```text
PDF
 │
 ▼
Extract Text (PyMuPDF)
 │
 ▼
Gemini API
 │
 ▼
Structured JSON
 │
 ▼
Pydantic Validation
 │
 ▼
Save JSON
```

---

# 📥 Sample Input

```
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
Chennai

Reporting Manager:
Rahul Sharma

Benefits
• Health Insurance
• Provident Fund
• Performance Bonus
```

---

# 📤 Sample Output

```json
{
    "company_name": "TechVision Technologies Private Limited",
    "offer_date": "10 October 2026",
    "document_type": "OFFER LETTER",
    "candidate_name": "Arun Kumar",
    "position": "AI Software Engineer",
    "employee_id": "TVT1026",
    "department": "Artificial Intelligence",
    "joining_date": "01 November 2026",
    "annual_ctc": "₹12,00,000",
    "work_location": "Chennai, Tamil Nadu",
    "reporting_manager": "Rahul Sharma",
    "benefits": [
        "Health Insurance",
        "Provident Fund",
        "Performance Bonus"
    ]
}
```

---

# 📸 Demo

## Console Output

```
STEP 1 : Extracting Text from PDF

STEP 2 : Generating Structured JSON using Gemini

STEP 3 : Validating JSON

✅ JSON Validation Successful

STEP 4 : Saving JSON

✅ Saved to data/output/output.json

🎉 PROJECT COMPLETED SUCCESSFULLY
```

> 📷 Add screenshots of your terminal and `output.json` here after uploading your project.

---

# 💡 Future Improvements

- Support multiple document types
- OCR support for scanned PDFs
- Batch PDF processing
- Streamlit web application
- REST API using FastAPI
- Docker support
- Unit testing with pytest
- Confidence score for extracted fields

---

# 🎯 Skills Demonstrated

- Python Programming
- Prompt Engineering
- Large Language Models (LLMs)
- Google Gemini API
- JSON Processing
- Pydantic Validation
- PDF Parsing
- Error Handling
- Environment Variables
- Software Design

---

# 👨‍💻 Author

**Srivasan**

- GitHub: https://github.com/srivasan16
- LinkedIn: https://www.linkedin.com/in/sri-vasan-87b29126/

---

# ⭐ If you found this project useful, please give it a star!