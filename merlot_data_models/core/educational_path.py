from pydantic import BaseModel
from typing import Optional, List

from merlot_data_models.core.educational_step import EducationalStep

class EducationalPath(BaseModel):
    educationalSteps: List[EducationalStep]