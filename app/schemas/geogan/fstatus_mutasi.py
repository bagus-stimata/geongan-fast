from pydantic import BaseModel, ConfigDict
from datetime import datetime


class FStatusMutasiBase(BaseModel):
    kode1: str
    kode2: str
    description: str
    statusActive: bool = True
    model_config = ConfigDict(from_attributes=True, validate_by_name=True)

class FStatusMutasiCreate(FStatusMutasiBase):
    id: int

class FStatusMutasiUpdate(FStatusMutasiBase):
    id: int

class FStatusMutasiResponse(FStatusMutasiBase):
    id: int
    created: datetime
    modified: datetime
