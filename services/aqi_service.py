import httpx

async def aqi_data(lat: str, lon: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://air-quality-api.open-meteo.com/v1/air-quality?latitude={lat}&longitude={lon}&current=us_aqi")
        info = response.json()
        return info.get("current", {}).get("us_aqi")                            
                                    