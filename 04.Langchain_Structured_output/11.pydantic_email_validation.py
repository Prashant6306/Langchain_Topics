
from pydantic import BaseModel,EmailStr

class StudentInfo(BaseModel):
    name:str
    age:int
    email:EmailStr

#student1=StudentInfo(name="ganesh",age=25,email="abc@gmail.com")
student1=StudentInfo(name="ganesh",age=25,email="abc@gmail.com")
print(student1.name)
print(student1.age)
print(student1.email)

