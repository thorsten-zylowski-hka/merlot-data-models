from typing import List, Optional
from pydantic import BaseModel

from merlot_data_models.core.document import Document

class CertificateAttributes(BaseModel):
    title: str
    certifingOrganization: str
    documents: Optional[List[Document]]
    issueDate: Optional[str]
    expiryDate: Optional[str]
    type: Optional[List[str]]
    level: Optional[str]
    grade: Optional[str]

class Certificate(BaseModel):
    identifier: str
    attributes: CertificateAttributes
