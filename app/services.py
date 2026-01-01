from geoip2.database import Reader
from typing import Union

from utils import parse_user_agent
from .schema import Response, ErrorResponse

GEOIP_DATABASE_PATH = "./db/GeoLite2-City.mmdb"


def get_ip_info(ip_address: str, user_agent: str) -> Union[Response, ErrorResponse]:
    try:
        with Reader(GEOIP_DATABASE_PATH) as reader:
            response = reader.city(ip_address)

            data = {
                "success": True,
                "status": 200,
                "client_ip": ip_address,
                "country": response.country.name,
                "city": response.city.name,
                "latitude": response.location.latitude,
                "longitude": response.location.longitude,
                "time_zone": response.location.time_zone,
                "continent": response.continent.names.get("en"),
                "posta_code": response.postal.code,
                "isp": response.traits.isp,
                "organization": response.traits.organization,
                "user_agent": {
                    "user_agent_str": user_agent,
                    **parse_user_agent(user_agent),
                },
            }

        return Response(**data)

    except Exception as e:
        return ErrorResponse(
            success=False,
            status=400,
            error=str(e),
            user_agent={
                "user_agent_str": user_agent,
                **parse_user_agent(user_agent),
            },
        )
