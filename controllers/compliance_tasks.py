from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload
from typing import List
from datetime import datetime

from models.user import UserModel
from models.business import BusinessModel
from models.compliance_task import ComplianceTaskModel, TaskStatusEnum
from serializers.compliance_task import ComplianceTaskCreate, ComplianceTaskUpdate, ComplianceTaskSchema
from database import get_db
from dependencies.get_current_user import get_current_user

router=APIRouter()

@router.post('/businesses/{business_id}/compliance-tasks', response_model=ComplianceTaskSchema, status_code=status.HTTP_201_CREATED)
def create_compliance_task(
    business_id: int,
    task: ComplianceTaskCreate,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    
    # Check if the business exists and belongs to the user
    business = db.query(BusinessModel).filter(
        BusinessModel.id == business_id,
        BusinessModel.user_id == current_user.id
    ).first()
    
    if not business:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Business not found'
        )
    
    # Create new task for the business
    new_task = ComplianceTaskModel(
        title=task.title,
        description=task.description,
        due_date=task.due_date,
        status=task.status,
        submission_date=task.submission_date,
        business_id=business_id
    )
    
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    
    return new_task
    

@router.get('/businesses/{business_id}/compliance-tasks', response_model=List[ComplianceTaskSchema])
def get_compliance_tasks(
    business_id: int,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    
    # Check if the business exists and belongs to the user
    business = db.query(BusinessModel).filter(
        BusinessModel.id == business_id,
        BusinessModel.user_id == current_user.id
    ).first()
    
    if not business:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Business not found'
        )
    # if exists run the query and show 
    tasks = db.query(ComplianceTaskModel).options(
        joinedload(ComplianceTaskModel.business)
    ).filter(ComplianceTaskModel.business_id == business_id).all()
    
    return tasks

@router.get('/businesses/{business_id}/compliance-tasks/{task_id}', response_model=ComplianceTaskSchema)
def get_single_compliance_task(
    business_id: int,
    task_id: int,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    
    # Check if the business exists and belongs to the user
    business = db.query(BusinessModel).filter(
        BusinessModel.id == business_id,
        BusinessModel.user_id == current_user.id
    ).first()
    
    if not business:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Business not found'
        )
    
    # if exists run the query and show one task
    task = db.query(ComplianceTaskModel).filter(
        ComplianceTaskModel.id == task_id,
        ComplianceTaskModel.business_id == business_id
    ).first()
    
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Compliance task not found'
        )
    
    return task
