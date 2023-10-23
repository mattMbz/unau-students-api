import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Loading environment variables
load_dotenv()

# SQLAlchemy configurations
SQLALCHEMY_DATABASE_URL = os.getenv('HOST_CONNECTION')
engine = create_engine(SQLALCHEMY_DATABASE_URL)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
