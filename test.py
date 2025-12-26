from datetime import date, datetime, timezone
from database import SessionLocal
from models.user import UserModel
from models.business import BusinessModel, IndustryEnum
from models.license import LicenseModel, LicenseStatusEnum
from models.compliance_task import ComplianceTaskModel, TaskStatusEnum

def main():
    db = SessionLocal()
    try:
        # Check if the test user already exists
        user = db.query(UserModel).filter_by(username="testuser12").first()
        if not user:
            user = UserModel(username="testuser12", email="test12@test.com")
            user.set_password("password123")
            db.add(user)
            db.commit()
            db.refresh(user)

        # Check if the business already exists for this user
        business = db.query(BusinessModel).filter_by(cr_number="CR12344").first()
        if not business:
            business = BusinessModel(
                name="Test Business",
                description="A test business",
                cr_number="CR12344",
                industry=IndustryEnum.IT_SOFTWARE,
                user_id=user.id
            )
            db.add(business)
            db.commit()
            db.refresh(business)

        # Create a license only if it doesn't exist
        license = db.query(LicenseModel).filter_by(name="Test License", business_id=business.id).first()
        if not license:
            license = LicenseModel(
                name="Test License",
                description="A test license",
                issue_date=datetime(2025, 1, 1, tzinfo=timezone.utc),
                expiry_date=datetime(2026, 1, 1, tzinfo=timezone.utc),
                status=LicenseStatusEnum.VALID,
                business_id=business.id
            )
            db.add(license)
            db.commit()
            db.refresh(license)

        # Create a compliance task only if it doesn't exist
        task = db.query(ComplianceTaskModel).filter_by(title="Test Compliance Task", business_id=business.id).first()
        if not task:
            task = ComplianceTaskModel(
                title="Test Compliance Task",
                description="Complete the compliance report",
                due_date=datetime(2025, 12, 31, tzinfo=timezone.utc),
                status=TaskStatusEnum.PENDING,
                business_id=business.id
            )
            db.add(task)
            db.commit()
            db.refresh(task)

        # Check the data
        print(f"User: {user.username}")
        print(f"Businesses: {len(user.businesses)}")
        print(f"Licenses for business: {len(business.licenses)}")
        print(f"Compliance tasks for business: {len(business.compliance_tasks)}")

        # Test CASCADE - delete the user
        db.delete(user)
        db.commit()

        # Check if license and tasks were deleted
        remaining_business = db.query(BusinessModel).filter(BusinessModel.id == business.id).first()
        remaining_license = db.query(LicenseModel).filter(LicenseModel.id == license.id).first()
        remaining_task = db.query(ComplianceTaskModel).filter(ComplianceTaskModel.id == task.id).first()

        print(f"Business still exists: {remaining_business is not None}")  
        print(f"License still exists: {remaining_license is not None}")  
        print(f"Compliance task still exists: {remaining_task is not None}")

    except Exception as e:
        db.rollback()
        print(f"Error: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    main()