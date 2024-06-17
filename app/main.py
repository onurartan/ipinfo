from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from geoip2.database import Reader

from func import parse_user_agent

app = FastAPI()

# GeoLite2 veritabanı dosyasının yolu
GEOIP_DATABASE_PATH = "./db/GeoLite2-City.mmdb"


# GeoLite2 veritabanı okuyucusunu oluşturun
reader = Reader(GEOIP_DATABASE_PATH)


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def index():
    return {
        "message": "Welcome to the free IP address city, country, etc. learning API"
    }


@app.get("/getip")
def get_client_ip(request: Request):
    client_ip = request.client.host

    return client_ip


@app.get("/yourinfo")
def get_client_ip(request: Request):
    client_ip = request.client.host

    try:
        # IP adresinden coğrafi bilgi alın
        response = reader.city(client_ip)
        country = response.country.name
        city = response.city.name
        latitude = response.location.latitude
        longitude = response.location.longitude
        continent = response.continent.names["en"]
        time_zone = response.location.time_zone
        postal = response.postal.code

        # User-Agent başlığını al
        user_agent = request.headers.get("User-Agent")

        return {
            "client_ip": client_ip,
            "country": country,
            "city": city,
            "latitude": latitude,
            "longitude": longitude,
            "time_zone": time_zone,
            "continent": continent,
            "posta_code": postal,
            "user_agent": {
                "user_agent_str": user_agent,
                **parse_user_agent(user_agent),
            },
        }
    except Exception as e:
        user_agent = request.headers.get("User-Agent")
        return {
            "error": str(e),
            "user_agent": {
                "user_agent_str": user_agent,
                **parse_user_agent(user_agent),
            },
        }


@app.get("/ipinfo")
def get_client_ip(ip: str, request: Request):

    try:
        # IP adresinden coğrafi bilgi alın
        response = reader.city(ip)
        country = response.country.name
        city = response.city.name
        latitude = response.location.latitude
        longitude = response.location.longitude
        continent = response.continent.names["en"]
        time_zone = response.location.time_zone
        postal = response.postal.code

        # User-Agent başlığını al
        user_agent = request.headers.get("User-Agent")

        return {
            "client_ip": ip,
            "country": country,
            "city": city,
            "latitude": latitude,
            "longitude": longitude,
            "time_zone": time_zone,
            "continent": continent,
            "posta_code": postal,
            "user_agent": {
                "user_agent_str": user_agent,
                **parse_user_agent(user_agent),
            },
        }
    except Exception as e:
        return {"error": str(e)}
