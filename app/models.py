from pydantic import BaseModel
from typing import List, Dict, Any

class DocumentUpload(BaseModel):
    filename: str
    doc_type: str
    content: str

class MultiDocQuery(BaseModel):
    question: str
    filter_type: str = "all"
