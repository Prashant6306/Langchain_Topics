
from pydantic import BaseModel

class Person(BaseModel):
    name:str
    age:int
    salary:float

new_person=Person(name="Ganesh",age=25,salary=10000.1)

print(new_person)