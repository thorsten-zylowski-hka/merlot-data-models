from pydantic import BaseModel


class Document(BaseModel):
    documentURI: str
    title: str