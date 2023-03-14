from pydantic import BaseModel
from typing import Optional

from merlot_data_models.core.educational_level import EducationalLevel
from merlot_data_models.core.name import Name

class Skill(BaseModel):
    name: Name
    educationalFramework: Optional[str]
    educationalLevel: Optional[str]
    alternateName: Optional[str]
    description: Optional[str]
    url: Optional[str]
    targetUrl: Optional[str]