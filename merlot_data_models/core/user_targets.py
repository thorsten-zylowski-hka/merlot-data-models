from typing import List
from pydantic import BaseModel

class EducationalTarget(BaseModel):
    fieldOfSpecification: List[str]
    target: List[str]

class UserTargets(BaseModel):
    educationalTarget: EducationalTarget
    careerTargets: List[str]
    positionChangeReasons: List[str]
    personalRequirements: List[str]