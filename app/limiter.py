from slowapi import Limiter
from  slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

# Limiter Configuration
GLOBAL_API_RATE_LIMIT = "75/minute"

PER_MINUTES_5 = "5/minute"
PER_MINUTES_10 = "10/minute"
PER_MINUTES_15 = "15/minute"
PER_MINUTES_25 = "25/minute"
PER_MINUTES_75 = "75/minute"
PER_MINUTES_100 = "100/minute"
PER_MINUTES_200 = "200/minute"
