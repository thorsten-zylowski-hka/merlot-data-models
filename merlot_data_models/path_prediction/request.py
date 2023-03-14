from pydantic import BaseModel

from merlot_data_models.core.cognitive_position import CognitivePosition


class PathPredictionRequest(BaseModel):
    cognitivePosition: CognitivePosition