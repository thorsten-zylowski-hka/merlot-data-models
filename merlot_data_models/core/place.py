from pydantic import BaseModel
from typing import Optional


class Place(BaseModel):
    name: str
    address: Optional[str]
    longitude: Optional[float]
    latitude: Optional[float]