from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from models.compliance_task import TaskStatusEnum

class ComplianceTaskCreate(BaseModel):
    title: str=Field(...,min_length=1,max_length=255)
    description:str
    due_date:datetime
    status:TaskStatusEnum=TaskStatusEnum.PENDING
    submission_date:Optional[datetime]=None

class ComplianceTaskUpdate(BaseModel):
    title: Optional[str]=Field(None,min_length=1,max_length=255)
    description:Optional[str]=None
    due_date: Optional[datetime] = None
    status: Optional[TaskStatusEnum] = None
    submission_date: Optional[datetime] = None


class ComplianceTaskSchema(BaseModel):
    id: int
    title: str
    description: str
    due_date: datetime
    submission_date: Optional[datetime]
    status: TaskStatusEnum
    business_id: int
    created_at: datetime

    class Config:
        from_attributes = True