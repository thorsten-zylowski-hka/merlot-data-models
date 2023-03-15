from pydantic import BaseModel
from typing import List, Optional
from merlot_data_models.core.certificate import Certificate
from merlot_data_models.core.place import Place

class EducationalStepAttributes(BaseModel):
    identifier: str
    name: str
    description: str
    contentLocation: Optional[Place]
    keywords: Optional[List[str]]
    certificate: Optional[Certificate]
    startDate: Optional[str]
    endDate: Optional[str]
    status: Optional[str]

class EducationalStep(BaseModel):
    identifier: str
    type: str
    attributes: EducationalStepAttributes