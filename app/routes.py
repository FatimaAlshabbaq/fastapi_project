from fastapi import APIRouter

router = APIRouter()

@router.get("/hello")
def hello():
    return {"message": "Hello, World!"}

@router.get("/square/{number}")
def square(number: int):
    return {"number": number, "square": number * number}

@router.get("/reverse/{text}")
def reverse(text: str):
    return {"original": text, "reversed": text[::-1]}