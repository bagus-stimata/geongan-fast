from pydantic import BaseModel, ConfigDict
from typing import Optional


class FCompanyBase(BaseModel):
    kode1: str
    description: Optional[str] = None
    status_active: bool = True
    model_config = ConfigDict(from_attributes=True)


class FCompanyCreate(FCompanyBase):
    id: int


class FCompanyResponse(FCompanyBase):
    id: int
