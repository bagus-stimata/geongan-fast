from pydantic import BaseModel, ConfigDict
from typing import Optional


class CompanyBase(BaseModel):
    kode1: str
    description: Optional[str] = None
    status_active: bool = True
    model_config = ConfigDict(from_attributes=True)


class CompanyCreate(CompanyBase):
    id: int


class CompanyResponse(CompanyBase):
    id: int
