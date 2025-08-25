from datetime import datetime
from pydantic import BaseModel, ConfigDict
from typing import Optional


class FDatasetBase(BaseModel):
    kode1: str
    description: Optional[str] = None
    division_id: int
    status_active: bool = True
    avatar_image: Optional[str] = None
    tr_date: Optional[datetime] = None
    private: bool = False
    relation_key_to_geo: Optional[str] = None
    sumber_data: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)


class FDatasetCreate(FDatasetBase):
    id: int


class FDatasetResponse(FDatasetBase):
    id: int

