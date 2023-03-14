from pydantic import BaseModel
from typing import Optional

from merlot_data_models.core.educational_level import EducationalLevel
from merlot_data_models.core.name import Name

class SkillAttribtes(BaseModel):
    name: Name
    educationalFramework: str
    educationalLevel: EducationalLevel
    alternateName: Optional[str]
    description: str
    url: Optional[str]
    targetUrl: Optional[str]

class Skill(BaseModel):
    skill: SkillAttribtes