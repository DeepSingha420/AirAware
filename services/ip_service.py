from fastapi import Request
import httpx


async def read_ip(request: Request, ip:str = None):
    if ip:
        return ip
    forwarded = request.headers.get("X-Forwarded-For")
    if forwarded:
        # The first IP in the list is the original client
        return forwarded.split(",")[0].strip()
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.ipify.org?format=text")

        return response.text

async def public_ip():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.ipify.org?format=text")

        return response.text

