# ProxyJWT
Small proxy service written with FastAPI

## General Info
HTTP Proxy that forwards a POST request to the upstream host and adds a JWT token to the request headers.
<br/>
### JWT Creation
 JWT token is created having the following claims:
  - iat - Timestamp of the request as specified by the specification
  - jti - A cryptographic nonce that should be unique
  - payload - A json payload of the structure: {"user": "username", "date": "todays date"}
<br/>
  Algorithm used by default is HS512 unless otherwise specified in .env
  Secret used by default is also configurable through .env

## File Structure
```
.
├── Dockerfile
├── Makefile
├── README.md
├── docker-compose.yml
└── src
    ├── main.py
    ├── requirements.txt
    ├── services
    │   ├── jwt.py
    │   └── upstream.py
    └── test_main.py
```

	
## Libraries used
Requirements.txt:
* uvicorn
* fastapi
* httpx
* pyjwt
* python-decouple
* pytest
* requests

`Docker image using Python 3.8`
	
## Setup and running
Commands for running and testing are kept inside Makefile.

To just build the proxy container:
```
$ make build
```
To start the proxy container with docker-compose:
```
$ make run
```
To test the two async requests:
```
$ make test
```
