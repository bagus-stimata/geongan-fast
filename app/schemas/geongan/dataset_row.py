from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date


class DatasetRowBase(BaseModel):
    kode1: Optional[str] = None
    description: Optional[str] = None
    dataset_id: int
    fsatuan_id: Optional[int] = None
    evalue_type: Optional[str] = None
    str_value1: Optional[str] = None
    int_value1: Optional[int] = None
    double_value1: Optional[float] = None
    date_value1: Optional[date] = None
    model_config = ConfigDict(from_attributes=True)


class DatasetRowCreate(DatasetRowBase):
    id: int


class DatasetRowResponse(DatasetRowBase):
    id: int
