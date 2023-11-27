from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from datetime import datetime
import bcrypt


Base = declarative_base()
engine = create_engine("postgresql://marsuvees:987654321@localhost:5432/blog_marsuvees")
session = sessionmaker(engine)()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=True, unique=True)
    phone_number = Column(String, nullable=True)
    date_of_birth = Column(DateTime, nullable=True)
    password = Column(String, nullable=False)

if __name__ == "__main__":
    admin = User(username="admin", password=bcrypt.hashpw("admin".encode("utf-8"), bcrypt.gensalt()).decode("utf-8"))
    session.add(admin)
    session.commit()




    