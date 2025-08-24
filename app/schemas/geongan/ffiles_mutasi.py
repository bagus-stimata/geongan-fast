from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime


class FFilesMutasiBase(BaseModel):
    kode1: str
    kode2: str
    description: str
    fileName: Optional[str] = ""
    fileSize: Optional[int] = 0
    statusActive: bool = True
    model_config = ConfigDict(from_attributes=True, validate_by_name=True)

class FFilesMutasiCreate(FFilesMutasiBase):
    id: int

class FFilesMutasiUpdate(FFilesMutasiBase):
    id: int

class FFilesMutasiResponse(FFilesMutasiBase):
    id: int
    created: datetime
    modified: datetime
