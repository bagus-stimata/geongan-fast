from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime


class FProsesMutasiBase(BaseModel):
    kode1: str
    kode2: str
    description: str
    hashPath: Optional[str] = ""
    ffilesMutasiBean: Optional[int] = 0
    fstatusMutasiBean: Optional[int] = 0
    statusActive: bool = True
    model_config = ConfigDict(from_attributes=True, validate_by_name=True)

class FProsesMutasiCreate(FProsesMutasiBase):
    id: int

class FProsesMutasiUpdate(FProsesMutasiBase):
    id: int

class FProsesMutasiResponse(FProsesMutasiBase):
    id: int
    created: datetime
    modified: datetime
