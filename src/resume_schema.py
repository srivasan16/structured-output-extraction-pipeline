from pydantic import BaseModel
from typing import List


class OfferLetter(BaseModel):
    company_name: str
    offer_date: str
    document_type: str
    candidate_name: str
    position: str
    employee_id: str
    department: str
    joining_date: str
    annual_ctc: str
    work_location: str
    reporting_manager: str
    benefits: List[str]