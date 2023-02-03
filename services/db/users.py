from sqlalchemy.orm import Session
from sqlalchemy import select

from models.users import User
from schemas.users import CreateUserSchema



def create_user(session:Session, user:CreateUserSchema):
	db_user = User(**user.dict())
	session.add(db_user)
	session.commit()
	session.refresh(db_user)
	return db_user


def list_users(session:Session):
	return session.query(User).all()


def get_user(session:Session, email:str):
	return session.query(User).filter(User.email == email).one()


def get_user_by_id(session:Session, id:int):
	return session.query(User).filter(User.id == id).one()
