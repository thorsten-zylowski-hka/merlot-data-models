from pydantic import BaseModel
from typing import List

from merlot_data_models.core.educational_path import EducationalPath
from merlot_data_models.core.formal_educational_step import FormalEducationalStep

class PathPredictionResponse(BaseModel):
    educationals_paths: List[EducationalPath]
    formal_educational_paths: List[List[FormalEducationalStep]]