# generated by datamodel-codegen:
#   filename:  AirbyteInternal.yaml

from __future__ import annotations

from pydantic import BaseModel, Extra, Field
from typing_extensions import Literal


class AirbyteInternal(BaseModel):
    class Config:
        extra = Extra.forbid

    field_sl: Literal[100, 200, 300] = Field(..., alias="_sl")
    field_ql: Literal[100, 200, 300, 400, 500, 600] = Field(..., alias="_ql")
