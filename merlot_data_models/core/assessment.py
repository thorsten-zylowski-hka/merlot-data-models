from typing import List

from pydantic import BaseModel


class AssessmentCluster(BaseModel):
    label: str
    score: float

class Assessment(BaseModel):
    identifier: str
    framework: str
    clusters: List[AssessmentCluster]