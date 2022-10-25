from pydantic import BaseModel
from typing import Optional

from educational_graph_node import EducationalGraphNode
from learning_object import LearningObject

class UserGoal(BaseModel):
    formalGoal: EducationalGraphNode
    specificGoal: LearningObject