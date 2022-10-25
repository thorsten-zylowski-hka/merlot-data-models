from pydantic import BaseModel
from typing import Optional
from core.user_cognitive_position import UserCognitivePosition
from core.user_goal import UserGoal
from core.user_requirements import UserRequirements

class PathPredictionRequest(BaseModel):
    cognitive_position: UserCognitivePosition
    goal: UserGoal
    requirements: UserRequirements