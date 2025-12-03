from __future__ import annotations

from typing import Literal, Optional

from pydantic import BaseModel, Field


Base64Mode = Literal["encode", "decode"]
HashAlgorithm = Literal["md5", "sha1", "sha256", "sha512"]
TimestampMode = Literal["unix_to_human", "human_to_unix"]
JsonYamlDirection = Literal["json_to_yaml", "yaml_to_json"]


class Base64Request(BaseModel):
    payload: str = Field(..., description="原始字符串")
    mode: Base64Mode = "encode"


class Base64Response(BaseModel):
    result: str


class HashRequest(BaseModel):
    payload: str
    algorithm: HashAlgorithm = "md5"


class HashResponse(BaseModel):
    algorithm: HashAlgorithm
    hash: str


class TimestampRequest(BaseModel):
    value: str
    mode: TimestampMode
    timezone: Optional[str] = Field(
        default=None, description="IANA 时区, 默认使用本地"
    )


class TimestampResponse(BaseModel):
    unix: int
    human: str


class JsonFormatRequest(BaseModel):
    payload: str
    indent: int = Field(default=2, ge=0, le=8)


class JsonFormatResponse(BaseModel):
    formatted: str
    size: int


class JsonYamlRequest(BaseModel):
    payload: str
    direction: JsonYamlDirection = "json_to_yaml"


class JsonYamlResponse(BaseModel):
    result: str


class ColorConvertRequest(BaseModel):
    value: str = Field(..., description="支持 Hex (#ff00ff)、RGB 或 HSL 字符串")


class ColorConvertResponse(BaseModel):
    hex: str
    rgb: str
    hsl: str


DiffType = Literal["added", "removed", "unchanged"]


class DiffLine(BaseModel):
    type: DiffType
    value: str


class TextDiffRequest(BaseModel):
    left: str = Field("", description="原文本")
    right: str = Field("", description="对比文本")


class TextDiffResponse(BaseModel):
    diff: list[DiffLine]
