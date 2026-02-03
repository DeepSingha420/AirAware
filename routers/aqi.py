from fastapi import APIRouter, Request
from models.schemas import Result
from services.ip_service import public_ip
from services.geo_service import geo_ip
from services.aqi_service import aqi_data

router = APIRouter()

@router.get("/aqi")
async def give_aqi(request: Request, Response_model=Result):
    ip = await read_ip()
    geo_data = await geo_ip(ip)
    aqi_info = await aqi_data(geo_data.get("latitude"), geo_data.get("longitude"))
    aqi_cat = "Unknown"
    if int(aqi_info)<50:
        aqi_cat = "Good"
    elif int(aqi_info)<100:
        aqi_cat = "Moderate"
    elif int(aqi_info)<150:
        aqi_cat = "Unhealthy for Sensitive Groups"
    elif int(aqi_info)<200:
        aqi_cat = "Unhealthy"
    elif int(aqi_info)<300:
        aqi_cat = "Very Unhealthy"
    else:
        aqi_cat = "Hazardous"
    return {
        "ip": geo_data.get("ip"),
        "location":{
            "city": geo_data.get("city"),
            "region": geo_data.get("region"),
            "country": geo_data.get("country"),
            "lat": geo_data.get("latitude"),
            "lon": geo_data.get("longitude"),
        },
        "aqi":{
            "value": aqi_info,
            "category": aqi_cat
        },
        "source": "open-meteo"
    }



