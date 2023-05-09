from pydantic import BaseModel
from typing import List

from merlot_data_models.core.occupation import Occupation

class OccupationsResponse(BaseModel):
    occupations: List[Occupation]