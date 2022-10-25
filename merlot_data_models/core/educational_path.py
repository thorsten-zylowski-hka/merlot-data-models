from pydantic import BaseModel
from typing import Optional, List
from core.learning_object import LearningObject

class EducationalPath(BaseModel):
    start: LearningObject
    end: LearningObject
    stations: Optional[List[LearningObject]]