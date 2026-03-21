

from pydantic import BaseModel
from typing import Optional

class StudentInfo(BaseModel):
    name:str
    list1:bool

student1=StudentInfo(name="santosh",indian="True")
print(student1.name)
print(student1.indian)