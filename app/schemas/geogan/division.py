from pydantic import BaseModel, ConfigDict
from typing import Optional


class DivisionBase(BaseModel):
    kode1: str
    description: Optional[str] = None
    company_id: int
    status_active: bool = True
    model_config = ConfigDict(from_attributes=True)


class DivisionCreate(DivisionBase):
    id: int


class DivisionResponse(DivisionBase):
    id: int
