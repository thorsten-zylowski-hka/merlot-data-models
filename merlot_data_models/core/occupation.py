from pydantic import BaseModel
from typing import List, Optional

from merlot_data_models.core.cognitive_position import CognitivePosition

class OccupationAttributes(BaseModel):
    name: str
    url: Optional[str]
    description: Optional[str]


class Occupation(BaseModel):
    identifier: str
    type = "Occupation"
    attributes: OccupationAttributes