from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session


from ecom import db
from ecom.user import hashing
from ecom.user.models import User

from .jwt import create_access_token

router = APIRouter(tags=['auth'])


@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db_session: Session = Depends(db.get_db)):
    user = db_session.query(User).filter(User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid Credentials')

    if not hashing.verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid Password')

    # Generate a JWT Token
    access_token = create_access_token(data={"sub": user.email})

    return {"access_token": access_token, "token_type": "bearer"}
