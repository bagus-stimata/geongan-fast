from pydantic import BaseModel, ConfigDict
from datetime import datetime


class FDeptBase(BaseModel):
    kode1: str
    kode2: str
    description: str
    fdivisionBean: int
    statusActive: bool = True
    model_config = ConfigDict(from_attributes=True, validate_by_name=True)

class FDeptCreate(FDeptBase):
    id: int

class FDeptUpdate(FDeptBase):
    id: int

class FDeptResponse(FDeptBase):
    id: int
    created: datetime
    modified: datetime
