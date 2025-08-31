from fastapi import FastAPI
from app.api.routes.health import router as health_router
from app.api.routes.sum import router as sum_router
from app.api.routes.payslips import router as payslip_router

app = FastAPI(title="Payslips Lab")
app.include_router(health_router)
app.include_router(sum_router)
app.include_router(payslip_router)
