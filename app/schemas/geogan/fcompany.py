from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime


class FCompanyBase(BaseModel):
    kode1: str
    kode2: str
    description: str
    alamat1: Optional[str] = ""
    alamat2: Optional[str] = ""
    telp: Optional[str] = ""
    email: Optional[str] = ""
    website: Optional[str] = ""
    statusActive: bool = True
    model_config = ConfigDict(from_attributes=True, validate_by_name=True)

class FCompanyCreate(FCompanyBase):
    id: int

class FCompanyUpdate(FCompanyBase):
    id: int

class FCompanyResponse(FCompanyBase):
    id: int
    created: datetime
    modified: datetime
