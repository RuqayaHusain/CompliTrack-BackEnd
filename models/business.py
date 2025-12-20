from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Enum as SQLEnum
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from .base import BaseModel
from enum import Enum
from .compliance_task import ComplianceTaskModel

class IndustryEnum(str, Enum):
    RETAIL = "Retail"
    FOOD_BEVERAGE = "Food & Beverage"
    CONSTRUCTION = "Construction"
    HEALTHCARE = "Healthcare"
    EDUCATION = "Education"
    IT_SOFTWARE = "IT / Software"
    MANUFACTURING = "Manufacturing"
    LOGISTICS = "Logistics"
    PROFESSIONAL_SERVICES = "Professional Services"

class BusinessModel(BaseModel):
    __tablename__ = "businesses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)  # Text allows longer content than String
    cr_number = Column(String(50), nullable=False, unique=True)
    industry = Column(SQLEnum(IndustryEnum, name='industry_enum'), nullable=False)
    image_url = Column(Text, nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    # Foreign key linking to users table
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)

    # Relationships - these let us access related data easily!
    user = relationship('UserModel', back_populates='businesses')
    licenses = relationship('LicenseModel', back_populates='business', cascade='all, delete-orphan')
    compliance_tasks = relationship('ComplianceTaskModel', back_populates='business', cascade='all, delete-orphan')