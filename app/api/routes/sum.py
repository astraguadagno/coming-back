from fastapi import APIRouter
from app.schemas.sum import SumRequest, SumResponse

router = APIRouter()

@router.post("/sumar", response_model=SumResponse)
def sumar(payload: SumRequest):
    r = payload.a + payload.b
    return SumResponse(a=payload.a, b=payload.b, resultado=r)
