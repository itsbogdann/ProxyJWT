from decouple import config
from datetime import datetime
from uuid import uuid4
import jwt

JWT_SECRET=config("JWT_SECRET", default="a9ddbcaba8c0ac1a0a812dc0c2f08514b23f2db0a68343cb8199ebb38a6d91e4ebfb378e22ad39c2d01 d0b4ec9c34aa91056862ddace3fbbd6852ee60c36acbf")
JWT_ALGORITHM=config("JWT_ALGORITHM", default="HS512")

"""
Helper function which combines user claims and generates JWT token
"""
def sign_JWT():

    now = datetime.utcnow()

    jwtClaims = {
        "iat": now,
        "jti": uuid4().hex,
        "payload": {
                "username": 'proxyUser' + str(uuid4().hex),
                "date": now.strftime("%Y-%m-%d")
            }
    }

    return jwt.encode(jwtClaims, JWT_SECRET, algorithm=JWT_ALGORITHM)
