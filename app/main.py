from fastapi import FastAPI, Request
from geoip2.database import Reader

app = FastAPI()

# GeoLite2 veritabanı dosyasının yolu
GEOIP_DATABASE_PATH = './db/GeoLite2-City.mmdb'


# GeoLite2 veritabanı okuyucusunu oluşturun
reader = Reader(GEOIP_DATABASE_PATH)

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

        return {
            "client_ip": client_ip,
            "country": country,
            "city": city,
            "latitude": latitude,
            "longitude": longitude
        }
    except Exception as e:
        return {"error": str(e)}
    
@app.get("/ipinfo")
def get_client_ip(ip: str,request: Request):

    try:
        # IP adresinden coğrafi bilgi alın
        response = reader.city(ip)
        country = response.country.name
        city = response.city.name
        latitude = response.location.latitude
        longitude = response.location.longitude

        return {
            "client_ip": ip,
            "country": country,
            "city": city,
            "latitude": latitude,
            "longitude": longitude
        }
    except Exception as e:
        return {"error": str(e)}