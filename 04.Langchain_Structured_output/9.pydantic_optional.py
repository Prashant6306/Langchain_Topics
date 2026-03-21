
from pydantic import BaseModel
from typing import Optional

class StudentInfo(BaseModel):
    name:str
    age:Optional[int]=None

student1=StudentInfo(name="rajesh")
print(student1.name)
print(student1.age)