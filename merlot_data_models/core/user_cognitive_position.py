from pydantic import BaseModel
from typing import Optional

from core.educational_graph_node import EducationalGraphNode
from core.learning_object import LearningObject
from core.educational_path import EducationalPath

class UserCognitivePosition(BaseModel):
    formalPosition: EducationalGraphNode
    latestLearningObject: LearningObject
    historyOfEducation: EducationalPath