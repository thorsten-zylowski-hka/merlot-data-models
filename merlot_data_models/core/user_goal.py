from pydantic import BaseModel
from typing import Optional

from core.educational_graph_node import EducationalGraphNode
from core.learning_object import LearningObject

class UserGoal(BaseModel):
    formalGoal: EducationalGraphNode
    specificGoal: LearningObject