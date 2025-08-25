from enum import IntEnum
from typing import Optional

from pydantic import BaseModel, ConfigDict, model_validator


class EndpointType(IntEnum):
    PUBLIC = 0
    PRIVATE = 1
    INTERNAL = 2


class FtEndpointAccessBase(BaseModel):
    userBean: int
    endpoint: str
    fdatasetBean: int
    endPointType: EndpointType
    basicAuth: Optional[str] = None

    model_config = ConfigDict(from_attributes=True, use_enum_values=True)

    @model_validator(mode="after")
    def check_basic_auth(self):
        if self.endPointType in (EndpointType.PRIVATE, EndpointType.INTERNAL) and not self.basicAuth:
            raise ValueError("basicAuth required for PRIVATE or INTERNAL endpoints")
        if self.endPointType == EndpointType.PUBLIC and self.basicAuth is not None:
            raise ValueError("basicAuth must be null for PUBLIC endpoints")
        return self


class FtEndpointAccessCreate(FtEndpointAccessBase):
    id: int


class FtEndpointAccessResponse(FtEndpointAccessBase):
    id: int

