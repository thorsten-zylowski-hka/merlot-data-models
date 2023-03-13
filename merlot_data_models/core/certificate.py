from typing import List
from pydantic import BaseModel

from merlot_data_models.core.document import Document

class CertificateAttributes(BaseModel):
    title: str
    certifingOrganization: str
    documents: List[Document]
    issueDate: str
    expiryDate: str
    type: List[str]
    level: str
    grade: str

class Certificate(BaseModel):
    identifier: str
    attributes: CertificateAttributes
