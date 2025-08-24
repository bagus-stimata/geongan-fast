from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime


class FFilesLainnyaBase(BaseModel):
    kode1: str
    kode2: str
    description: str
    fileName: Optional[str] = ""
    fileSize: Optional[int] = 0
    statusActive: bool = True
    model_config = ConfigDict(from_attributes=True, validate_by_name=True)

class FFilesLainnyaCreate(FFilesLainnyaBase):
    id: int

class FFilesLainnyaUpdate(FFilesLainnyaBase):
    id: int

class FFilesLainnyaResponse(FFilesLainnyaBase):
    id: int
    created: datetime
    modified: datetime
