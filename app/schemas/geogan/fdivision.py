from pydantic import BaseModel, ConfigDict
from datetime import datetime


class FDivisionBase(BaseModel):
    kode1: str
    kode2: str
    description: str
    fcompanyBean: int
    statusActive: bool = True
    model_config = ConfigDict(from_attributes=True, validate_by_name=True)

class FDivisionCreate(FDivisionBase):
    id: int

class FDivisionUpdate(FDivisionBase):
    id: int

class FDivisionResponse(FDivisionBase):
    id: int
    created: datetime
    modified: datetime
