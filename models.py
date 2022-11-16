from typing import Optional, List
from pydantic import BaseModel


class ValidItem(BaseModel):
    id: Optional[str]
    content: Optional[str]
    link_type: Optional[str]


class Item(BaseModel):
    category: Optional[ValidItem]
    description: Optional[ValidItem]
    next_inspection: Optional[ValidItem]
    operator: Optional[ValidItem]
    ordz: Optional[ValidItem]
    site: Optional[ValidItem]


class SearchData(BaseModel):
    data: List[Item]
    