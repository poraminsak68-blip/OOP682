from models.classroom import ClassRoom
from models.student import Student

oop = ClassRoom("OOP")

oop.add_students(Student(1, "Alice", 20, "S001"))
oop.add_students(Student(2, "Bob", 22, "S002"))

print(f'{oop.name} registered {len(oop)} students')

oop.add_students(Student(3, "Charlie", 21, "S003"))

print(len(oop))

print('Students in the class:')
for i in range(len(oop)):
    print(oop[i])
