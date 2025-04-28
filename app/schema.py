from pydantic import BaseModel
from typing import Optional


class Response(BaseModel):
    success: bool
    status: int
    client_ip: str
    country: Optional[str] = None
    city: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    time_zone: Optional[str] = None
    continent: Optional[str] = None
    posta_code: Optional[str] = None
    isp: Optional[str] = None
    organization: Optional[str] = None
    user_agent: dict


class ErrorResponse(BaseModel):
    success: bool
    status: int
    error: str
    user_agent: dict
