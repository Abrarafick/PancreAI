from pydantic import BaseModel
from datetime import datetime


class CTScanResponse(BaseModel):
    id: int
    user_id: int
    file_name: str
    file_type: str
    file_path: str
    uploaded_at: datetime

    class Config:
        from_attributes = True