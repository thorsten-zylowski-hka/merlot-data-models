from pydantic import BaseModel
from typing import Optional
from merlot_data_models.core.user_cognitive_position import UserCognitivePosition
from merlot_data_models.core.user_goal import UserGoal
from merlot_data_models.core.user_requirements import UserRequirements

class PathPredictionRequest(BaseModel):
    cognitive_position: UserCognitivePosition
    goal: UserGoal
    requirements: UserRequirements