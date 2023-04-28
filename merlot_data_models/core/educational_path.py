from pydantic import BaseModel
from typing import List, Optional

from merlot_data_models.core.educational_step import EducationalStep
from merlot_data_models.core.educational_step import EducationalStepExplanation

class EducationalPath(BaseModel):
    educationalSteps: List[EducationalStep]
    explanations: Optional[List[EducationalStepExplanation]]