import jwt
from datetime import datetime, timedelta, timezone

from fastapi import HTTPException, status

JWT_SECRET = "4cb59e8beef5fc214df3f691a863334e"

# access_token 발급
def create_access_token(user_id: int) -> str:
    payload = {
        "sub": str(user_id),
        "exp": datetime().now(timezone.utc) + timedelta(hours=24)    
    }

    return jwt.encode(
        payload=payload, key=JWT_SECRET, algorithm="HS256"
    )

# access_token의 위변조 여부 확인 & payload 읽는 함수
def verify_access_token(access_token: str) -> dict:

    try:
        payload = jwt.decode(
        access_token, JWT_SECRET, algorithms=["HS256"],
    )
    except jwt.DecodeError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="잘못된 토큰 형식입니다.",
        )
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="만료된 토큰입니다.",
        )

    return
