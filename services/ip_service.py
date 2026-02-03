from fastapi import Request
import httpx


async def read_ip(request: Request):
    forwarded = request.headers.get("X-Forwarded-For")
    if forwarded:
        # The first IP in the list is the original client
        return forwarded.split(",")[0].strip()
    return request.client.host

async def public_ip():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.ipify.org?format=text")
        return response.text