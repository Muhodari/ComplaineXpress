from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    department = Column(String(255))
    sectors = Column(String(255))
    role = Column(String(50))
    user_status = Column(Enum('ACTIVE', 'LOCKED', name='user_status_enum'), default='ACTIVE')
    phone_number = Column(String(20))
    full_name = Column(String(255))

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}', " \
               f"department='{self.department}', sectors='{self.sectors}', role='{self.role}', " \
               f"user_status='{self.user_status}', phone_number='{self.phone_number}', " \
               f"full_name='{self.full_name}')>"
