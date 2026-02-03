from pydantic import BaseModel

class Location(BaseModel):
    city: str
    region: str
    country: str
    lat: float
    lon: float

class Aqi(BaseModel):
    value: int
    category: str

class Result(BaseModel):
    ip: str
    location: Location
    aqi: Aqi
    source: str = "open-meteo"
