from geoip2.database import Reader

from utils import parse_user_agent
from .schema import Response, ErrorResponse

GEOIP_DATABASE_PATH = "./db/GeoLite2-City.mmdb"

reader = Reader(GEOIP_DATABASE_PATH)


def get_ip_info(ip_address: str, user_agent: str) -> Response | ErrorResponse:
    try:
        # Get geographic info from IP address
        response = reader.city(ip_address)
        country = response.country.name
        city = response.city.name
        latitude = response.location.latitude
        longitude = response.location.longitude
        continent = response.continent.names["en"]
        time_zone = response.location.time_zone
        postal = response.postal.code
        isp = response.traits.isp  # ISP bilgisi
        organization = response.traits.organization  # Organizasyon
        reader.close()

        data = {
            "success": True,
            "status": 200,
            "client_ip": ip_address,
            "country": country,
            "city": city,
            "latitude": latitude,
            "longitude": longitude,
            "time_zone": time_zone,
            "continent": continent,
            "posta_code": postal,
            "isp": isp,
            "organization": organization,
            "user_agent": {
                "user_agent_str": user_agent,
                **parse_user_agent(user_agent),
            },
        }

        return Response(**data)
    except Exception as e:

        error_data = {
            "success": False,
            "status": 400,
            "error": str(e),
            "user_agent": {
                "user_agent_str": user_agent,
                **parse_user_agent(user_agent),
            },
        }
        return ErrorResponse(**error_data)
