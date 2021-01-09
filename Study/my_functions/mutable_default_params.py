from typing import List, Optional

class Student:
    def __init__(self, name:str, grades: Optional[List[int]] = None): 
    #def __init__(self, name:str, grades: List[int] = None): 
    #def __init__(self, name:str, grades: List[int] = []): 
        # it is bad -- when the function is create -- it create a list and that is assigned to self.grades
        # it means all instance share the list
        # not use mutable default values
        self.name = name
        self.grades = grades or []

    def take_exam(self, result):
        self.grades.append(result)


bob = Student("Bob")
bob.take_exam(99)
bob.take_exam(77)
print(bob.grades)

john = Student("John")
print(john.grades)

