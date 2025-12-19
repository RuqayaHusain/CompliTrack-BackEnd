from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session, joinedload
from typing import List, Optional

from models.business import BusinessModel, IndustryEnum
from models.user import UserModel
from serializers.business import BusinessCreate, BusinessUpdate, BusinessSchema
from database import get_db
from dependencies.get_current_user import get_current_user

# Create the router
router = APIRouter()

@router.post('/businesses', response_model=BusinessSchema, status_code=status.HTTP_201_CREATED)
def create_business(
    business: BusinessCreate,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    # Create new business instance
    new_business = BusinessModel(
        name=business.name,
        description=business.description,
        cr_number=business.cr_number,
        industry=business.industry,
        image_url=business.image_url,
        user_id=current_user.id
    )

    # Check if business with the same CR number exists
    existing_business = db.query(BusinessModel).filter(
        BusinessModel.cr_number == business.cr_number
    ).first()

    if existing_business:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Business with this CR number already exists'
        )

    # Add to database
    db.add(new_business)
    db.commit()
    db.refresh(new_business) # Refresh to get the generated id and created_at

    return new_business

@router.get('/businesses', response_model=List[BusinessSchema])
def get_businesses(
    name: Optional[str] = Query(None, description='Filter by business name'),
    industry: Optional[IndustryEnum] = Query(None, description='Filter by business industry'),
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
    ):
    filtered_businesses = db.query(BusinessModel).options(
        joinedload(BusinessModel.user),
        joinedload(BusinessModel.licenses)
    ).filter(BusinessModel.user_id == current_user.id)

    if name:
        filtered_businesses = filtered_businesses.filter(BusinessModel.name.ilike(f"%{name}%"))
    if industry:
        filtered_businesses = filtered_businesses.filter(BusinessModel.industry == industry)

    all_businesses = filtered_businesses.all()

    return all_businesses

@router.get('/businesses/{business_id}', response_model=BusinessSchema)
def get_single_business(
    business_id: int,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    business = db.query(BusinessModel).filter(
        BusinessModel.id == business_id,
        BusinessModel.user_id == current_user.id
        ).first()

    if not business:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Business not found'
        )
    
    return business

# Placeholder route to test the router
@router.get('/businesses/test')
def test_businesses_router():
    """Test endpoint to verify the businesses router is working"""
    return {"message": "Businesses router is working! Ready for CRUD operations."}