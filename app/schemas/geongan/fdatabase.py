from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime


class FDatabaseBase(BaseModel):
    kode1: str
    kode2: str
    description: str
    version: Optional[int] = 0
    uuid: Optional[str] = ""
    vendorDb: Optional[str] = ""
    serverOs: Optional[str] = ""
    statusActive: bool = True
    fcompanyBean: int
    dbVersion: Optional[str] = ""
    serverData: Optional[str] = ""
    model_config = ConfigDict(from_attributes=True, validate_by_name=True)

class FDatabaseCreate(FDatabaseBase):
    id: int

class FDatabaseUpdate(FDatabaseBase):
    id: int

class FDatabaseResponse(FDatabaseBase):
    id: int
    created: datetime
    modified: datetime
