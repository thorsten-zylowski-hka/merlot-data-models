from pydantic import BaseModel
from typing import Dict, Optional


class OccupationAttributes(BaseModel):
    name: str
    url: Optional[str]
    description: Optional[str]
    riasec: Optional[Dict[str,float]]


class Occupation(BaseModel):
    identifier: str
    type: str = "Occupation"
    attributes: OccupationAttributes