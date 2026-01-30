class ClassRoom:
    def __init__(self,name):
        self.name = name
        self.students = []

    def add_students(self,students):
        self.students.append(students)

    def __len__(self):
        return len(self.students)
    
    def __getattribute__(self, index):
        return self.students[index]