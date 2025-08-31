from fastapi import APIRouter
from app.schemas.payslips import PayslipsRequest, PayslipsResponse
router = APIRouter()

@router.post("/payslips", response_model=PayslipsResponse)
def compute_days_worked(payslipData : PayslipsRequest):
    days_worked = int(payslipData.hours / 7.6)
    return PayslipsResponse(user_id=payslipData.user_id, 
                            hours= payslipData.hours, 
                            date=payslipData.date, 
                            days_worked= days_worked )

