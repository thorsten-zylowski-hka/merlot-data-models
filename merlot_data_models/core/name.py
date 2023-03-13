from pydantic import BaseModel


class Name(BaseModel):
    inLanguage: str
    name: str