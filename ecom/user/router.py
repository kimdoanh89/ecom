from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ecom import db

from . import schema, services, validator

router = APIRouter(tags=["Users"], prefix="/user")


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user_registration(
    request: schema.User, db_session: Session = Depends(db.get_db)
):
    user = await validator.verify_email_exit(request.email, db_session)

    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system.",
        )

    new_user = await services.new_user_register(request, db_session)
    return new_user
