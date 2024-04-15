from sqlalchemy import Column, Integer, String, Text, Enum
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Complain(Base):
    __tablename__ = 'complain'

    id = Column(Integer, primary_key=True)
    sector_id = Column(Integer)
    sector_name = Column(String(255))
    department_id = Column(Integer)
    department_name = Column(String(255))
    complain_text = Column(Text)
    phone_number = Column(String(20))
    email_address = Column(String(255))
    status = Column(Enum('PENDING', 'REJECTED', 'APPROVED'))
