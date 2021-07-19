from datetime import datetime
from fastapi import Request, Response, FastAPI
app =FastAPI()

from services.jwt import sign_JWT
from services.upstream import upstream_post

INITIAL_TIME = datetime.now()
UPSTREAM_POSTS = 0

"""
POST request that creates a JWT token, passes it further to upstream host
and returns the upstream result back
"""
@app.post("/")
async def root_post(req: Request):
    global UPSTREAM_POSTS
    UPSTREAM_POSTS += 1

    body = await req.json()
    token = sign_JWT()
    upstream_response = await upstream_post(body, token, req.headers)

    return Response(headers=upstream_response.headers, status_code=upstream_response.status_code, content=upstream_response.content)


"""
GET request that returns time passed since uptime and number of passed upstream POST requests
"""
@app.get("/status")
async def get_status():
    time_diff = datetime.now() - INITIAL_TIME
    upstream_posts = UPSTREAM_POSTS

    elapsed_time = {
        "minutes": round(time_diff.total_seconds () / 60),
        "seconds": round(time_diff.total_seconds())
    }

    return { "elapsed_time": elapsed_time, "upstream_posts": upstream_posts }
