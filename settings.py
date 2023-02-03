import os
import cloudinary

# Database url configuration
DATABASE_URL = "postgresql+psycopg2://{username}:{password}@{host}:{port}/{db_name}".format(
	host=os.getenv("POSTGRES_HOST"),
	port=os.getenv("POSTGRES_PORT"),
	db_name=os.getenv("POSTGRES_DB"),
	username=os.getenv("POSTGRES_USER"),
	password=os.getenv("POSTGRES_PASSWORD"),
)

config = cloudinary.config(secure=True)


SECRET_KEY = os.getenv("SECRET_KEY")
