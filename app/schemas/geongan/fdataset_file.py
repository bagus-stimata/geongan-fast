from pydantic import BaseModel, ConfigDict
from typing import Optional


class FDatasetFileBase(BaseModel):
    fdataset_id: int
    file_name: str
    file_type: Optional[str] = None
    jenis: Optional[str] = None
    flag: Optional[str] = None
    description: Optional[str] = None
    kode1: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)


class FDatasetFileCreate(FDatasetFileBase):
    id: int


class FDatasetFileResponse(FDatasetFileBase):
    id: int

