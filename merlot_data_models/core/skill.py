from pydantic import BaseModel
from merlot_data_models.core.educational_level import EducationalLevel

from merlot_data_models.core.name import Name

class SkillAttribtes(BaseModel):
    name: Name
    educationalFramework: str
    url: str
    educationalLevel: EducationalLevel
    alternateName: str
    description: str
    url: str
    targetUrl: str

class Skill(BaseModel):
    skill: SkillAttribtes