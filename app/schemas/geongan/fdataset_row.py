from datetime import date
from pydantic import BaseModel, ConfigDict
from typing import Optional


class FDatasetRowBase(BaseModel):
    kode1: Optional[str] = None
    description: Optional[str] = None
    fdataset_id: int
    fsatuan_id: Optional[int] = None
    evalue_type: Optional[str] = None
    str_value1: Optional[str] = None
    int_value1: Optional[int] = None
    double_value1: Optional[float] = None
    date_value1: Optional[date] = None
    model_config = ConfigDict(from_attributes=True)


class FDatasetRowCreate(FDatasetRowBase):
    id: int


class FDatasetRowResponse(FDatasetRowBase):
    id: int

