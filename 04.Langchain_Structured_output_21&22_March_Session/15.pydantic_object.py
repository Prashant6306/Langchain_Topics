from pydantic import BaseModel

class StudentInfo(BaseModel):
    name: str
    age: int

student = StudentInfo(name='Alice', age=30)
print(type(student))
# Convert to dictionary
student_dict = student.model_dump()
print("Dict:", student_dict)
print("Age:", student_dict['age'])
print(type(student_dict))

# Convert to JSON string
# student_json = student.model_dump_json()
# print("JSON:", student_json)
# print(type(student_json))