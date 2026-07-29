from fastapi import APIRouter
from app.schemas.user import UserLogin


router = APIRouter()


@router.post("/login")
def login(user: UserLogin):

    return {
        "message": "Login API working",
        "email": user.email
    }