# IP Information Retrieval with FastAPI and Rate Limiting

This project provides a simple FastAPI service that retrieves information about an IP address, such as the country, city, latitude, longitude, and more. It uses the GeoIP2 database and has rate-limiting functionality to prevent excessive requests. 

You can also integrate this API with external services like [ipinfo.trymagic.xyz](https://ipinfo.trymagic.xyz/docs) if you prefer not to host your own instance.

## Features
- Retrieve detailed information about an IP address including geolocation (country, city, continent, latitude, longitude, postal code, etc.)
- Rate limiting to avoid abuse of the API with global request limits.
- Support for CORS to allow external domains to access the API.
- Custom error handling for rate limit exceedance.

## Endpoints

### `/`
This is the root endpoint that provides a welcome message and basic information about the service.

**Example Response:**
```json
{
  "message": "Welcome to the free IP address city, country, etc. learning API",
  "client_ip": "203.0.113.42",
  "country": "United States",
  "city": "New York",
  "latitude": 40.7128,
  "longitude": -74.0060,
  "continent": "North America",
  "time_zone": "America/New_York",
  "postal_code": "10001",
  "user_agent": {
    "user_agent_str": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
  }
}
```

### `/getip`
This endpoint returns the client's public IP address.

**Example Response:**
```json
{
  "ip_address": "203.0.113.42"
}
```

### `/yourinfo`
This endpoint retrieves detailed information about the client's IP address, including country, city, geographical coordinates, and user agent details.

**Example Response:**
```json
{
  "client_ip": "203.0.113.42",
  "country": "United States",
  "city": "New York",
  "latitude": 40.7128,
  "longitude": -74.0060,
  "continent": "North America",
  "time_zone": "America/New_York",
  "postal_code": "10001",
  "user_agent": {
    "user_agent_str": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
  }
}
```

### `/ipinfo`
This endpoint allows users to query any IP address for detailed information about that IP.

**Parameters:**
- `ip` (str): The IP address for which you want to retrieve information.

**Example Response:**
```json
{
  "client_ip": "203.0.113.42",
  "country": "United States",
  "city": "New York",
  "latitude": 40.7128,
  "longitude": -74.0060,
  "continent": "North America",
  "time_zone": "America/New_York",
  "postal_code": "10001",
  "user_agent": {
    "user_agent_str": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
  }
}
```

## Rate Limiting

To prevent abuse of the API, this service implements rate limiting for all endpoints using the [slowapi](https://github.com/laurentS/slowapi) library. This library helps manage the rate limits globally, and the limit is defined by the constant `GLOBAL_API_RATE_LIMIT`. If the rate limit is exceeded, the service returns a `429 Too Many Requests` error.

### Example of Rate Limit Exceeded Error Response
```json
{
  "detail": {
    "success": false,
    "status": 429,
    "error": "rate_limit_exceeded",
    "msg": "Rate limit exceeded, try again later"
  }
}
```

## Installation

### Prerequisites
- Python 3.8+
- FastAPI
- Uvicorn (ASGI server)
- GeoIP2 database for IP information
- `slowapi` for rate-limiting functionality

### Installation Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/ip-info-fastapi.git
   cd ip-info-fastapi
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

4. Your API will be running on `http://127.0.0.1:8000`.

## Testing the API

- You can test the API using **Swagger UI** available at `http://127.0.0.1:8000/docs`.
- Alternatively, use **Postman** or **curl** to make requests.

## Optional External API

If you prefer not to host your own instance of the API, you can use the public API at [https://ipinfo.trymagic.xyz/docs](https://ipinfo.trymagic.xyz/docs) for IP information.

## License

This project is open-source and free to use. Feel free to contribute or modify as needed.

## Notes

- Rate Limiting: The API is rate-limited globally to prevent misuse. You can adjust the rate limit configuration in the `limiter.py` file.
- External API: You can use [ipinfo.trymagic.xyz](https://ipinfo.trymagic.xyz/docs) as an external service if you don't want to manage your own server.

---

### Technology Stack
- **FastAPI**: A modern, fast web framework for building APIs with Python 3.8+ based on standard Python type hints.
- **Uvicorn**: ASGI server for running FastAPI applications.
- **GeoIP2**: Library used for getting geolocation information based on an IP address.
- **slowapi**: A rate-limiting tool for FastAPI applications.
