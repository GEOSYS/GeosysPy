from enum import Enum


class Collection(Enum):
    MODIS = "MODIS"
    SENTINEL_2 = "SENTINEL_2"
    LANDSAT_8 = "LANDSAT_8"
    WEATHER_FORECAST_DAILY = "WEATHER.FORECAST_DAILY"
    WEATHER_FORECAST_HOURLY = "WEATHER.FORECAST_HOURLY"
    WEATHER_HISTORICAL_DAILY = "WEATHER.HISTORICAL_DAILY"