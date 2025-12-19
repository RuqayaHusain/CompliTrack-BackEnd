from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Enum as SQLEnum
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from .base import BaseModel
from enum import Enum

class StatusEnum(str, Enum):
    VALID = "Valid"
    EXPIRED = "Expired"
    PENDING_RENEWAL = "Pending Renewal"

class LicenseModel(BaseModel):
    __tablename__ = "licenses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)  # Text allows longer content than String
    issue_date = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    expiry_date = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    status = Column(SQLEnum(StatusEnum, name='status_enum'), nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    # Foreign key linking to businesses table
    business_id = Column(Integer, ForeignKey('businesses.id', ondelete='CASCADE'), nullable=False)
    

    # Relationships - these let us access related data easily!
    business = relationship('BusinessModel', back_populates='licenses')
