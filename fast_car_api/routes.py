from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1/cars",
    tags=["cars"],
)

@router.get("/")
def list_car():
    return {
        'cars': [
            {"id": 1, "modelo": "Toyota Corolla"},
            {"id": 2, "modelo": "Honda Civic"},
            {"id": 3, "modelo": "Ford Focus"},
        ]
    }