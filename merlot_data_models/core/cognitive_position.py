from pydantic import BaseModel
from typing import List
from merlot_data_models.core.assessment import Assessment

from merlot_data_models.core.educational_step import EducationalStep
from merlot_data_models.core.interests import Interests
from merlot_data_models.core.skill import Skill
from merlot_data_models.core.user_targets import UserTargets
from merlot_data_models.core.working_step import WorkingStep

class CognitivePositionAttributes(BaseModel):
    educationalPathHistory: List[EducationalStep]
    workingHistory: List[WorkingStep]
    skills: List[Skill]
    interests: Interests
    userTargets: UserTargets
    personalAssessment: List[Assessment]

class CognitivePosition(BaseModel):
    identifier: str
    type = "Cognitive Position"
    attributes: CognitivePositionAttributes