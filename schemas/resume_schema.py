from pydantic import BaseModel
from typing import List


class OfferLetter(BaseModel):
    employee_name: str
    position: str
    employee_id: str
    department: str
    joining_date: str
    annual_ctc: str
    location: str
    reporting_manager: str
    benefits: List[str]
    company: str