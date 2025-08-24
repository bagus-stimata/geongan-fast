from pydantic import BaseModel, ConfigDict
from typing import Optional


class DatasetFileBase(BaseModel):
    dataset_id: int
    file_name: str
    file_type: Optional[str] = None
    jenis: Optional[str] = None
    flag: Optional[str] = None
    description: Optional[str] = None
    kode1: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)


class DatasetFileCreate(DatasetFileBase):
    id: int


class DatasetFileResponse(DatasetFileBase):
    id: int
