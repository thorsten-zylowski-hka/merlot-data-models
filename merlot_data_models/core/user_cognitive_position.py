from pydantic import BaseModel
from typing import Optional

from merlot_data_models.core.educational_graph_node import EducationalGraphNode
from merlot_data_models.core.learning_object import LearningObject
from merlot_data_models.core.educational_path import EducationalPath

class UserCognitivePosition(BaseModel):
    formalPosition: EducationalGraphNode
    latestLearningObject: LearningObject
    historyOfEducation: EducationalPath