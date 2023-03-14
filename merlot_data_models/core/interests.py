from typing import List, Optional
from pydantic import BaseModel


class Interests(BaseModel):
    personalInterests: Optional[List[str]]
    hobbies: Optional[List[str]]
    volunteering: Optional[List[str]]
    opinions: Optional[List[str]]