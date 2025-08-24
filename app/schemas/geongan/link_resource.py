from pydantic import BaseModel, ConfigDict


class LinkResourceBase(BaseModel):
    fdatasetFrom: int
    fdatasetTo: int
    model_config = ConfigDict(from_attributes=True)


class LinkResourceCreate(LinkResourceBase):
    id: int


class LinkResourceResponse(LinkResourceBase):
    id: int

