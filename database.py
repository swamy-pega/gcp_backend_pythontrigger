from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,Session
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base
import os
from dotenv import load_dotenv
from config import settings

# Replace with your actual DB URL
load_dotenv()

#api_url = os.getenv("API_URL")

#DATABASE_URL = os.getenv("DB_URL")

#DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_URL=settings.db_url
print("DB URL: "+DATABASE_URL)

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")

DB_NAME = os.getenv("DB_NAME", "postgres")
INSTANCE_CONNECTION_NAME = os.getenv("INSTANCE_CONNECTION_NAME", "turing-diode-477800-b0:northamerica-northeast2:postgresreact")


#DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@/{DB_NAME}?host=/cloudsql/{INSTANCE_CONNECTION_NAME}"


if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)


#DATABASE_URL = (f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@/{DB_NAME}?host={DB_HOST}")  

#DATABASE_URL = (
    #f"postgresql+psycopg2://postgres:{DB_PASSWORD}@/postgres"
    #"?host=/cloudsql/turing-diode-477800-b0:northamerica-northeast2:postgresreact")
#DATABASE_URL=settings.db_url
#print(" DB URL: "+DATABASE_URL) 
#DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@/{DB_NAME}?host=/cloudsql/{INSTANCE_CONNECTION_NAME}"
print(" DB URL: "+DATABASE_URL) 

#m/swamy-pega/python_api.git
engine = create_engine(DATABASE_URL)
print("Engine created successfully"+str(engine))
#turing-diode-477800-b0:northamerica-northeast2:postgresreact
# Session setup
SessionLocal = sessionmaker(autoflush=False,autocommit=False,bind=engine)
#session = SessionLocal()

Base = declarative_base()

# Create and insert a new user
#new_user = User(name="Alice", email="alice@example.com")
#session.add(new_user)
#session.commit()

# Query users
#users = session.query(User).all()
#for user in users:
  #  print(user.id, user.name, user.email)
def get_db():
   db = SessionLocal()
   try:
      yield db
   finally:
       db.close()
# Example usage
# with get_db() as db:
