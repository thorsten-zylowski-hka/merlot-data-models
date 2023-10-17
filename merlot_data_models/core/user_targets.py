from typing import List, Optional

from pydantic import BaseModel

from merlot_data_models.core.place import Place

class EducationalTarget(BaseModel):
    fieldOfSpecification: List[str]
    target: List[str]

class PreferredLocation(BaseModel):
    utterance: Optional[str]
    location: Optional[Place]

class UserTargets(BaseModel):
    educationalTarget: EducationalTarget
    careerTargets: List[str]
    positionChangeReasons: Optional[List[str]]
    personalRequirements: Optional[List[str]]
    preferredLocations: Optional[List[PreferredLocation]]