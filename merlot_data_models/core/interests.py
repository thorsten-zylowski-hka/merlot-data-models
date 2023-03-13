from typing import List
from pydantic import BaseModel


class Interests(BaseModel):
    personalInterests: List[str]
    hobbies: List[str]
    volunteering: List[str]
    opinions: List[str]