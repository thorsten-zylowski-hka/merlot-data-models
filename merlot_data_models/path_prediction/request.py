from pydantic import BaseModel
from typing import Optional
from merlot_data_models.core.cognitive_position import UserCognitivePosition

class PathPredictionRequest(BaseModel):
    cognitive_position: UserCognitivePosition