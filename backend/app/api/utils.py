from __future__ import annotations

import base64
import hashlib
import json
import re
from datetime import datetime, timezone
from difflib import SequenceMatcher
from typing import Iterable, Tuple

import yaml
from dateutil import parser
from fastapi import APIRouter, HTTPException, status

from app.models.utility import (
    Base64Request,
    Base64Response,
    ColorConvertRequest,
    ColorConvertResponse,
    DiffLine,
    HashRequest,
    HashResponse,
    JsonFormatRequest,
    JsonFormatResponse,
    JsonYamlRequest,
    JsonYamlResponse,
    TextDiffRequest,
    TextDiffResponse,
    TimestampRequest,
    TimestampResponse,
)

router = APIRouter(prefix="/utils", tags=["utilities"])


@router.post("/base64", response_model=Base64Response)
def base64_transform(payload: Base64Request) -> Base64Response:
    try:
        raw = payload.payload.encode("utf-8")
        if payload.mode == "encode":
            result = base64.b64encode(raw).decode("utf-8")
        else:
            result = base64.b64decode(raw).decode("utf-8")
    except (ValueError, UnicodeDecodeError) as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Base64 处理失败: {exc}",
        ) from exc
    return Base64Response(result=result)


@router.post("/hash", response_model=HashResponse)
def hash_string(payload: HashRequest) -> HashResponse:
    algorithms = {
        "md5": hashlib.md5,
        "sha1": hashlib.sha1,
        "sha256": hashlib.sha256,
        "sha512": hashlib.sha512,
    }

    hasher = algorithms[payload.algorithm]()
    hasher.update(payload.payload.encode("utf-8"))
    return HashResponse(algorithm=payload.algorithm, hash=hasher.hexdigest())


@router.post("/timestamp", response_model=TimestampResponse)
def convert_timestamp(payload: TimestampRequest) -> TimestampResponse:
    tzinfo = (
        timezone.utc
        if payload.timezone == "UTC"
        else datetime.now().astimezone().tzinfo
    )

    if payload.mode == "unix_to_human":
        try:
            unix = int(float(payload.value))
        except ValueError as exc:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="无效的 Unix 时间戳",
            ) from exc
        dt = datetime.fromtimestamp(unix, tz=timezone.utc).astimezone(tzinfo)
        return TimestampResponse(unix=unix, human=dt.isoformat())

    # human_to_unix
    try:
        dt = parser.isoparse(payload.value)
    except (ValueError, TypeError) as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="请输入有效的 ISO 时间，如 2024-05-01T12:00:00+08:00",
        ) from exc
    dt = dt.astimezone(tzinfo)
    unix = int(dt.timestamp())
    return TimestampResponse(unix=unix, human=dt.isoformat())


@router.post("/json/format", response_model=JsonFormatResponse)
def format_json(payload: JsonFormatRequest) -> JsonFormatResponse:
    try:
        parsed = json.loads(payload.payload)
    except json.JSONDecodeError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"JSON 解析失败: {exc}",
        ) from exc

    if payload.indent == 0:
        text = json.dumps(parsed, ensure_ascii=False, separators=(",", ":"))
    else:
        text = json.dumps(parsed, ensure_ascii=False, indent=payload.indent)

    return JsonFormatResponse(formatted=text, size=len(text.encode("utf-8")))


@router.post("/json-yaml", response_model=JsonYamlResponse)
def convert_json_yaml(payload: JsonYamlRequest) -> JsonYamlResponse:
    try:
        if payload.direction == "json_to_yaml":
            parsed = json.loads(payload.payload)
            result = yaml.safe_dump(parsed, allow_unicode=True, sort_keys=False)
        else:
            parsed = yaml.safe_load(payload.payload)
            result = json.dumps(parsed, ensure_ascii=False, indent=2)
    except (yaml.YAMLError, json.JSONDecodeError, TypeError) as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"转换失败: {exc}",
        ) from exc
    return JsonYamlResponse(result=result.strip())


COLOR_HEX_REGEX = re.compile(r"^#?(?P<hex>[0-9a-fA-F]{3}|[0-9a-fA-F]{6})$")
COLOR_RGB_REGEX = re.compile(
    r"rgb\(\s*(?P<r>\d{1,3})\s*,\s*(?P<g>\d{1,3})\s*,\s*(?P<b>\d{1,3})\s*\)", re.I
)
COLOR_HSL_REGEX = re.compile(
    r"hsl\(\s*(?P<h>\d{1,3})\s*,\s*(?P<s>\d{1,3})%\s*,\s*(?P<l>\d{1,3})%\s*\)", re.I
)


def _normalize_hex(short_hex: str) -> str:
    if len(short_hex) == 3:
        return "".join(ch * 2 for ch in short_hex)
    return short_hex


def _hsl_to_rgb(h: int, s: float, l: float) -> Tuple[int, int, int]:
    c = (1 - abs(2 * l - 1)) * s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = l - c / 2
    if h < 60:
        rp, gp, bp = c, x, 0
    elif h < 120:
        rp, gp, bp = x, c, 0
    elif h < 180:
        rp, gp, bp = 0, c, x
    elif h < 240:
        rp, gp, bp = 0, x, c
    elif h < 300:
        rp, gp, bp = x, 0, c
    else:
        rp, gp, bp = c, 0, x
    return tuple(round((channel + m) * 255) for channel in (rp, gp, bp))  # type: ignore


def _parse_color_to_rgb(value: str) -> Tuple[int, int, int]:
    value = value.strip()
    if match := COLOR_HEX_REGEX.match(value):
        hex_value = _normalize_hex(match.group("hex"))
        return tuple(int(hex_value[i : i + 2], 16) for i in (0, 2, 4))  # type: ignore
    if match := COLOR_RGB_REGEX.match(value):
        r, g, b = (int(match.group(k)) for k in ("r", "g", "b"))
        if any(channel > 255 for channel in (r, g, b)):
            raise ValueError("RGB 分量需在 0-255")
        return r, g, b
    if match := COLOR_HSL_REGEX.match(value):
        h = int(match.group("h")) % 360
        s = int(match.group("s")) / 100
        l = int(match.group("l")) / 100
        return _hsl_to_rgb(h, s, l)
    raise ValueError("仅支持 Hex、RGB、HSL (如 #ff00ff / rgb(1,2,3) / hsl(200,80%,40%))")


def _rgb_to_hex(r: int, g: int, b: int) -> str:
    return f"#{r:02x}{g:02x}{b:02x}"


def _rgb_to_hsl(r: int, g: int, b: int) -> Tuple[int, int, int]:
    rp, gp, bp = (channel / 255 for channel in (r, g, b))
    c_max = max(rp, gp, bp)
    c_min = min(rp, gp, bp)
    delta = c_max - c_min

    if delta == 0:
        h = 0
    elif c_max == rp:
        h = (60 * ((gp - bp) / delta) + 360) % 360
    elif c_max == gp:
        h = (60 * ((bp - rp) / delta) + 120) % 360
    else:
        h = (60 * ((rp - gp) / delta) + 240) % 360

    l = (c_max + c_min) / 2
    if delta == 0:
        s = 0
    else:
        s = delta / (1 - abs(2 * l - 1))

    return round(h), round(s * 100), round(l * 100)


@router.post("/color/convert", response_model=ColorConvertResponse)
def convert_color(payload: ColorConvertRequest) -> ColorConvertResponse:
    try:
        r, g, b = _parse_color_to_rgb(payload.value)
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)
        ) from exc

    hex_value = _rgb_to_hex(r, g, b)
    h, s, l = _rgb_to_hsl(r, g, b)

    return ColorConvertResponse(
        hex=hex_value,
        rgb=f"rgb({r}, {g}, {b})",
        hsl=f"hsl({h}, {s}%, {l}%)",
    )


def _build_diff_lines(before: Iterable[str], after: Iterable[str]) -> list[DiffLine]:
    matcher = SequenceMatcher(a=list(before), b=list(after))
    diff: list[DiffLine] = []
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "equal":
            diff.extend(
                DiffLine(type="unchanged", value=line) for line in matcher.a[i1:i2]
            )
        elif tag == "delete":
            diff.extend(DiffLine(type="removed", value=line) for line in matcher.a[i1:i2])
        elif tag == "insert":
            diff.extend(DiffLine(type="added", value=line) for line in matcher.b[j1:j2])
        elif tag == "replace":
            diff.extend(DiffLine(type="removed", value=line) for line in matcher.a[i1:i2])
            diff.extend(DiffLine(type="added", value=line) for line in matcher.b[j1:j2])
    return diff


@router.post("/text/diff", response_model=TextDiffResponse)
def diff_text(payload: TextDiffRequest) -> TextDiffResponse:
    before_lines = payload.left.splitlines()
    after_lines = payload.right.splitlines()
    diff = _build_diff_lines(before_lines, after_lines)
    return TextDiffResponse(diff=diff)
