from typing import List, Optional
from pydantic import BaseModel

from merlot_data_models.core.place import Place

class HiringOrganization(BaseModel):
    location: Place

class WorkingStepAttributes(BaseModel):
    identifier: str
    title: str
    description: str
    hiringOrganization: HiringOrganization
    keywords: Optional[List[str]]
    jobStartDate: Optional[str]
    jobEndDate: Optional[str]
    status: Optional[str]

class WorkingStep(BaseModel):
    identifier: str
    type: str
    attributes: WorkingStepAttributes
