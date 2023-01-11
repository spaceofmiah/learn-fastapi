import fastapi
from fastapi import Body, Depends
from sqlalchemy.orm import Session

from db_initializer import get_db
from models import users as user_model
from schemas.users import CreateUserSchema, UserSchema
from services.db import users as user_db_services


app = fastapi.FastAPI()


@app.post('/login')
def login():
	"""Processes user's authentication and returns a token
	on successful authentication.

	request body:

	- username: Unique identifier for a user e.g email, 
				phone number, name

	- password:
	"""
	return "ThisTokenIsFake"


@app.post('/signup', response_model=UserSchema)
def signup(
	payload: CreateUserSchema = Body(), 
	session:Session=Depends(get_db)
):
	"""Processes request to register user account."""
	payload.hashed_password = user_model.User.hash_password(payload.hashed_password)
	return user_db_services.create_user(session, user=payload)
