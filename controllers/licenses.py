from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session, joinedload
from typing import List, Optional
from datetime import datetime

from models.user import UserModel
from models.business import BusinessModel
from models.license import LicenseModel, LicenseStatusEnum
from serializers.license import LicenseCreate, LicenseSchema
from database import get_db
from dependencies.get_current_user import get_current_user

# Create the router
router = APIRouter()

@router.post('/businesses/{business_id}/licenses', response_model=LicenseSchema, status_code=status.HTTP_201_CREATED)
def create_license(
    business_id: int,
    license: LicenseCreate,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    # Check if business exists
    business = db.query(BusinessModel).filter(
        BusinessModel.id == business_id,
        BusinessModel.user_id == current_user.id,).first()
    if not business:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Business not found',
        )
    
    # Expiry date validation
    if license.expiry_date <= license.issue_date:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Expiry date must be after issue date',
        )

    # Create new license instance
    new_license = LicenseModel(
        name=license.name,
        description=license.description,
        issue_date=license.issue_date,
        expiry_date=license.expiry_date,
        status=license.status,
        business_id=business_id
    )    

    # Add to database
    db.add(new_license)
    db.commit()
    db.refresh(new_license) # Refresh to get the generated id and created_at

    return new_license

@router.get('/businesses/{business_id}/licenses', response_model=List[LicenseSchema])
def get_licenses(
    business_id: int,
    name: Optional[str] = Query(None, description='Filter by license name'),
    license_status: Optional[LicenseStatusEnum] = Query(None, description='Filter by license status'),
    expiry_before: Optional[datetime] = Query(None, description='Licenses expiring before this date'),
    expiry_after: Optional[datetime] = Query(None, description='Licenses expiring after this date'),
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    
    # Check if business exists
    business = db.query(BusinessModel).filter(
        BusinessModel.id == business_id,
        BusinessModel.user_id == current_user.id,
    ).first()
    if not business:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Business not found',
        )
    
    # Apply query if exists
    filtered_licenses = db.query(LicenseModel).options(
        joinedload(LicenseModel.business)
    ).filter(LicenseModel.business_id == business_id)
    
    if name:
        filtered_licenses = filtered_licenses.filter(LicenseModel.name.ilike(f"%{name}%"))

    if license_status:
        filtered_licenses = filtered_licenses.filter(LicenseModel.status == license_status)

    if expiry_before:
        filtered_licenses = filtered_licenses.filter(LicenseModel.expiry_date < expiry_before)

    if expiry_after:
        filtered_licenses = filtered_licenses.filter(LicenseModel.expiry_date > expiry_after)

    all_licenses = filtered_licenses.all()

    return all_licenses

@router.get('/businesses/{business_id}/licenses/{license_id}', response_model=LicenseSchema)
def get_single_license(
    business_id: int,
    license_id: int,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    # Check if business exists
    business = db.query(BusinessModel).filter(
        BusinessModel.id == business_id,
        BusinessModel.user_id == current_user.id,
    ).first()

    if not business:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Business not found',
        )
    
    # Check if license exists
    license = db.query(LicenseModel).filter(
        LicenseModel.id == license_id,
        LicenseModel.business_id == business_id,
        ).first()
    
    if not license:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='License not found',
        )
    
    return license
