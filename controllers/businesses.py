from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from models.business import BusinessModel
from models.user import UserModel
from serializers.business import BusinessCreate, BusinessUpdate, BusinessSchema
from database import get_db
from dependencies.get_current_user import get_current_user

# Create the router
router = APIRouter()

# We'll add routes here in the next lessons!

# Placeholder route to test the router
@router.get('/businesses/test')
def test_businesses_router():
    """Test endpoint to verify the businesses router is working"""
    return {"message": "Businesses router is working! Ready for CRUD operations."}