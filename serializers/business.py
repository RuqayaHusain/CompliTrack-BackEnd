from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from .user import UserResponseSchema
from models.business import IndustryEnum
from models.license import LicenseStatusEnum

class BusinessCreate(BaseModel):
    """Schema for creating a new business"""
    name: str = Field(..., min_length=1, max_length=255, description="Title of the Business")
    description: Optional[str] = Field(None, description="Description of the Business")
    cr_number: str = Field(..., min_length=1, max_length=50, description="CR Number of the Business")
    industry: IndustryEnum
    image_url: Optional[str] = Field(None, description="Business Logo")

    class Config:
        schema_extra = {
            "example": {
                "name": "My First Business!",
                "description": "A sample business description",
                "cr_number": "CR234",
                "industry": "RETAIL",
                "image_url": "https://img.freepik.com/free-vector/business-logo-template-minimal-branding-design-vector_53876-136229.jpg?semt=ais_hybrid&w=740&q=80"
            }
        }

class BusinessUpdate(BaseModel):
    """Schema for updating a business (all fields optional)"""
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = None
    industry: Optional[IndustryEnum] = None
    image_url: Optional[str] = None

    class Config:
        from_attributes = True
    

class LicenseSchema(BaseModel):
    """Basic License schema for nested display"""
    id: int
    name: str
    description: Optional[str] = None
    issue_date: datetime
    expiry_date: datetime
    status: LicenseStatusEnum
    created_at: datetime

    class Config:
        from_attributes = True

class BusinessSchema(BaseModel):
    """Schema for returning business data"""
    id: int
    name: str
    description: Optional[str] = None
    cr_number: str
    industry: IndustryEnum
    image_url: Optional[str] = None
    created_at: datetime
    user: UserResponseSchema
    licenses: List[LicenseSchema] = []

    class Config:
        from_attributes = True