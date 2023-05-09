from pydantic import BaseModel
from typing import List

from merlot_data_models.core.cognitive_position import CognitivePosition

class OccupationsRequest(BaseModel):
    cognitivePosition: CognitivePosition