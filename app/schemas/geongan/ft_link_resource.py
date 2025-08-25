from pydantic import BaseModel, ConfigDict


class FtLinkResourceBase(BaseModel):
    fdatasetFrom: int
    fdatasetTo: int
    model_config = ConfigDict(from_attributes=True)


class FtLinkResourceCreate(FtLinkResourceBase):
    id: int


class FtLinkResourceResponse(FtLinkResourceBase):
    id: int

