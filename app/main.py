from fastapi import FastAPI, Request, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from .services import get_ip_info
from .limiter import limiter, GLOBAL_API_RATE_LIMIT

from slowapi.errors import RateLimitExceeded
from slowapi import _rate_limit_exceeded_handler

app = FastAPI()


app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(RateLimitExceeded)
async def ratelimit_error(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=status.HTTP_429_TOO_MANY_REQUESTS,
        content={
            "detail": {
                "success": False,
                "status": 429,
                "error": "rate_limit_exceeded",
                "msg": "Rate limit exceeded, try again later",
            }
        },
    )


@app.get("/")
@limiter.limit(GLOBAL_API_RATE_LIMIT)
def index(request: Request):
    client_ip = request.client.host
    # User-Agent
    user_agent = request.headers.get("User-Agent")

    ip_info = get_ip_info(client_ip, user_agent)

    if ip_info.success:
        return {
            "message": "Welcome to the free IP address city, country, etc. learning API",
            **ip_info.model_dump(),
        }
    else:
        raise HTTPException(status_code=ip_info.status, detail=ip_info.model_dump())


@app.get("/getip")
@limiter.limit(GLOBAL_API_RATE_LIMIT)
def get_client_ip(request: Request):
    client_ip = request.client.host

    return {"ip_address": client_ip}


@app.get("/yourinfo")
@limiter.limit(GLOBAL_API_RATE_LIMIT)
def get_client_ip(request: Request):
    client_ip = request.client.host

    # User-Agent
    user_agent = request.headers.get("User-Agent")

    ip_info = get_ip_info(client_ip, user_agent)

    if ip_info.success:
        return ip_info.model_dump()
    else:
        raise HTTPException(status_code=ip_info.status, detail=ip_info.model_dump())


@app.get("/ipinfo")
@limiter.limit(GLOBAL_API_RATE_LIMIT)
def get_client_ip(ip: str, request: Request):

    # User-Agent
    user_agent = request.headers.get("User-Agent")

    ip_info = get_ip_info(ip, user_agent)

    if ip_info.success:
        return ip_info.model_dump()
    else:
        raise HTTPException(status_code=ip_info.status, detail=ip_info.model_dump())
