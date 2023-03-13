from pydantic import BaseModel


class Place(BaseModel):
    name: str
    address: str
    longitude: float
    latitude: float