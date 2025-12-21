from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from models.user import UserModel
from models.business import BusinessModel
from models.license import LicenseModel
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
    new_licesne = LicenseModel(
        name=license.name,
        description=license.description,
        issue_date=license.issue_date,
        expiry_date=license.expiry_date,
        status=license.status,
        business_id=business_id
    )    

    # Add to database
    db.add(new_licesne)
    db.commit()
    db.refresh(new_licesne) # Refresh to get the generated id and created_at

    return new_licesne