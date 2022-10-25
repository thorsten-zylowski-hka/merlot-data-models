from pydantic import BaseModel
from typing import List

from merlot_data_models.core.educational_path import EducationalPath

class PathPredictionResponse(BaseModel):
    educationals_paths: List[EducationalPath]