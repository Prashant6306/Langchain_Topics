

from typing import TypedDict

class Person(TypedDict):
    name:str
    age:int

new_person=Person(name="Ganesh",age="twenty-five")

print(new_person)