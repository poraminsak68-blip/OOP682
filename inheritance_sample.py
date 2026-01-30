from models.person import Person
from models.student import Student
from models.staff import Staff

person = Person(1234567890123, "John", 30)
student = Student(1234567890123, "Alice", 20, "S123")
staff = Staff(1234567890123, "Bob", 35, "ST456")
print(Person)
print(Student)
print(Staff)

def get_person_info(person):
    print(isinstance(person,Person))
    return f"Name:{person.name},Age:{person.age}"

get_person_info(student)
get_person_info(staff)

class Employee:
   pass