from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from models.license import LicenseStatusEnum

class LicenseCreate(BaseModel):
    """Schema for creating a new license"""
    name: str = Field(..., min_length=1, max_length=255, description="Title of the License")
    description: Optional[str] = Field(None, description="Description of the License")
    issue_date: datetime = Field(..., description="Issue date of the license")
    expiry_date: datetime = Field(..., description="Expiry date of the license")
    status: LicenseStatusEnum = Field(..., description="Current status of the license")
    business_id: int = Field(..., description="ID of the business this license belongs to")

    class Config:
        schema_extra = {
            "example": {
                "name": "Health & Safety License",
                "description": "Required safety license for the business",
                "issue_date": "2025-01-01T00:00:00Z",
                "expiry_date": "2026-01-01T00:00:00Z",
                "status": "VALID",
                "business_id": 1
            }
        }

class LicenseUpdate(BaseModel):
        """Schema for updating a license (all fields optional)"""
        name: Optional[str] = Field(None, min_length=1, max_length=255)
        description: Optional[str] = None
        issue_date: Optional[datetime] = None
        expiry_date: Optional[datetime] = None
        status: Optional[LicenseStatusEnum] = None

        class Config:
            from_attributes = True

class LicenseSchema(BaseModel):
    """Schema for returning license data"""
    id: int
    name: str
    description: Optional[str] = None
    issue_date: datetime
    expiry_date: datetime
    status: LicenseStatusEnum
    created_at: datetime
    business_id: int

    class Config:
        from_attributes = True