import httpx

async def geo_ip(ip: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://ipwho.is/{ip}")
        return response.json()