from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Enum as SQLEnum
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from .base import BaseModel
from enum import Enum

class TaskStatusEnum(str, Enum):
    PENDING = "Pending"
    SUBMITTED = "Submitted"
    LATE = "Late"

class ComplianceTaskModel(BaseModel):
    __tablename__ = "compliance_tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)  # Text allows longer content than String
    due_date = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    submission_date = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=True)
    status = Column(SQLEnum(TaskStatusEnum, name='task_status_enum'), nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    # Foreign key linking to businesses table
    business_id = Column(Integer, ForeignKey('businesses.id', ondelete='CASCADE'), nullable=False)
    

    # Relationships - these let us access related data easily!
    business = relationship('BusinessModel', back_populates='compliance_tasks')
