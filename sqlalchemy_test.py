from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pymysql
egine=create_engine(
    'mysql+pymysql://root:123456@localhost:3306/test3'
)
charset='utf8'
Base=declarative_base()
Session=sessionmaker(bind=egine)
session=Session()



class Student(Base):
    __tablename__ = 'students'
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(25),nullable=False)
    age=Column(Integer,nullable=False)
    gender=Column(String(25),nullable=False)
    def __repr__(self):
        return f'Student(id={self.id},name={self.name},age={self.age},gender={self.gender})'


session_query=session.query(Student).filter(Student.age>20).all()
for i in session_query:
    print(i)
session.close()

