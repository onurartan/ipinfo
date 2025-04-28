from pydantic import BaseModel
from typing import Optional


class Response(BaseModel):
    success: bool
    status: int
    client_ip: str
    country: str | None
    city: str | None
    latitude: float | None
    longitude: float | None
    time_zone: str | None
    continent: str | None
    posta_code: str | None
    isp: str | None
    organization: str | None
    user_agent: dict


class ErrorResponse(BaseModel):
    success: bool
    status: int
    error: str
    user_agent: dict
