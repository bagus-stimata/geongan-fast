from pydantic import BaseModel, ConfigDict
from typing import Optional


class FDivisionBase(BaseModel):
    kode1: str
    description: Optional[str] = None
    company_id: int
    status_active: bool = True
    model_config = ConfigDict(from_attributes=True)


class FDivisionCreate(FDivisionBase):
    id: int


class FDivisionResponse(FDivisionBase):
    id: int

