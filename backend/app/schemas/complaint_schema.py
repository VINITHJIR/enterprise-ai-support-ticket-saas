from pydantic import BaseModel

from app.enums.complaint_enum import (
    ComplaintCategory,
    ComplaintStatus
)


class CreateComplaintRequest(BaseModel):

    complaint: str

    category: ComplaintCategory


class ComplaintResponse(BaseModel):

    id: int

    complaint: str

    category: ComplaintCategory

    status: ComplaintStatus

    class Config:

        from_attributes = True

class ComplaintProcessResponse(BaseModel):

    is_duplicate: bool

    complaint: ComplaintResponse