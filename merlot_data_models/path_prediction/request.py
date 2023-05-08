from pydantic import BaseModel
from typing import List, Optional, Dict

from merlot_data_models.core.cognitive_position import CognitivePosition
from merlot_data_models.core.educational_step import EducationalStep
from merlot_data_models.core.formal_educational_step import FormalEducationalStep


class ExplanationConfiguration(BaseModel):
    calculateExplanations: bool
    calculateAlternatives: bool
    calculateFeatureImportance: bool

class PathPredictionRequestConfiguration(BaseModel):
    explanations: Optional[ExplanationConfiguration]

class PathPredictionHints(BaseModel):
    formalEducationalPath: Optional[List[FormalEducationalStep]]
    educationalSteps: Optional[Dict[FormalEducationalStep, EducationalStep]]

class PathPredictionRequest(BaseModel):
    cognitivePosition: CognitivePosition
    configuration: Optional[PathPredictionRequestConfiguration]
    hints: Optional[PathPredictionHints]