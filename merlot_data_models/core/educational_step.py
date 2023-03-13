from pydantic import BaseModel
from typing import List
from merlot_data_models.core.certificate import Certificate
from merlot_data_models.core.place import Place

class EducationalStepAttributes(BaseModel):
    identifier: str
    name: str
    description: str
    contentLocation: Place
    keywords: List[str]
    certificate: Certificate
    startDate: List[str]
    endDate: List[str]
    status: str

class EducationalStep(BaseModel):
    identifier: str
    type = str
    attributes: EducationalStepAttributes