from typing import Dict

import fastapi
from fastapi import Body, Depends, HTTPException, status
from sqlalchemy.orm import Session

from db_initializer import get_db
from models import users as user_model
from services.db import users as user_db_services
from schemas.users import CreateUserSchema, UserSchema, UserLoginSchema


app = fastapi.FastAPI()


@app.post('/login', response_model=Dict)
def login(
		payload: UserLoginSchema = Body(),
		session: Session = Depends(get_db)
	):
	"""Processes user's authentication and returns a token
	on successful authentication.

	request body:

	- username: Unique identifier for a user e.g email, 
				phone number, name

	- password:
	"""
	try:
		user:user_model.User = user_db_services.get_user(
			session=session, email=payload.email
		)
	except:
		raise HTTPException(
			status_code=status.HTTP_401_UNAUTHORIZED,
			detail="Invalid user credentials"
		)

	is_validated:bool = user.validate_password(payload.password)
	if not is_validated:
		raise HTTPException(
			status_code=status.HTTP_401_UNAUTHORIZED,
			detail="Invalid user credentials"
		)

	return user.generate_token()



@app.post('/signup', response_model=UserSchema)
def signup(
	payload: CreateUserSchema = Body(), 
	session:Session=Depends(get_db)
):
	"""Processes request to register user account."""
	payload.hashed_password = user_model.User.hash_password(payload.hashed_password)
	return user_db_services.create_user(session, user=payload)
