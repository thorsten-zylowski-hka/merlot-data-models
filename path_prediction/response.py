from pydantic import BaseModel
from typing import List

from core.educational_path import EducationalPath

class PathPredictionResponse(BaseModel):
    educationals_paths: List[EducationalPath]