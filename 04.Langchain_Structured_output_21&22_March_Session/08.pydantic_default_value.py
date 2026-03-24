
from pydantic import BaseModel

class StudentInfo(BaseModel):
    name:str="Akshay"
    age:int=25

student1=StudentInfo(name="Ganesh",age=30)
print(student1.name)
print(student1.age)