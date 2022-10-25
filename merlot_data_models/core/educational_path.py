from pydantic import BaseModel
from typing import Optional, List
from learning_object import LearningObject

class EducationalPath(BaseModel):
    start: LearningObject
    end: LearningObject
    stations: Optional[List[LearningObject]]