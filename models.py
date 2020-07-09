from sqlalchemy import Boolean, Column, Integer, String

from database import Base


class Photos(Base):
    __tablename__ = "photos"

    id = Column(Integer, primary_key=True, index=True)
    picId = Column(String, unique=True, index=True)
    picURL = Column(String, unique=True, index=True)

    # email = Column(String, unique=True, index=True)
    # hashed_password = Column(String)
    # is_active = Column(Boolean, default=True)