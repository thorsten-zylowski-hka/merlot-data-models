from pydantic import BaseModel
from typing import Optional

from educational_graph_node import EducationalGraphNode
from learning_object import LearningObject
from educational_path import EducationalPath

class UserCognitivePosition(BaseModel):
    formalPosition: EducationalGraphNode
    latestLearningObject: LearningObject
    historyOfEducation: EducationalPath