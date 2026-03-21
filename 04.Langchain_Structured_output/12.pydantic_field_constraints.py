

from pydantic import BaseModel, Field

class StudentInfo(BaseModel):
    name:str=Field(min_length=3,
                   max_length=20)
    age:int
    cgpa:float=Field(ge=0,
                     lt=10,
                     default=5.0,
                     description="A decimal valude representing the CGPA of student")
name="ganesh"*7
print(name)
student1=StudentInfo(name=name,age=20)

print(student1.name)
print(student1.age)
print(student1.cgpa)