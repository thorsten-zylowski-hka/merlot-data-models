from typing import List, Optional

from pydantic import BaseModel

from merlot_data_models.core.name import Name


class EducationalLevel(BaseModel):
    description: str
    name: List[Name]
    alternateName: Optional[str]
    educationalFramework: str
    url: str
    targetUrl: str
    type: str