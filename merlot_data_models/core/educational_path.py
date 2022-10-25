from pydantic import BaseModel
from typing import Optional, List
from merlot_data_models.core.learning_object import LearningObject

class EducationalPath(BaseModel):
    start: LearningObject
    end: LearningObject
    stations: Optional[List[LearningObject]]