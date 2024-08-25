from fastapi import APIRouter

router = APIRouter(
    prefix='/api/v1',
    tags=['common'],
)


@router.get("/test")
def get_test():
    return {"test": "success"}



