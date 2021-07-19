from decouple import config
import httpx

UPSTREAM_URL = config("UPSTREAM_URL", default="https://postman-echo.com/post")

"""
Helper function which handles async requests to the upstream host
and fetches the response
"""
async def upstream_post(body, token, headers):

    upstream_headers = {
        "content-type": headers["content-type"],
        "connection": headers["connection"],
        "user-agent": headers["user-agent"],
        "accept": headers["accept"],
        "x-my-jwt": token
    }

    async with httpx.AsyncClient() as client:
        upstream_response = await client.post(
            UPSTREAM_URL,
            data = body,
            headers = upstream_headers,
        )
        return upstream_response