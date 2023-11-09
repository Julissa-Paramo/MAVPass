class Student:

    def __init__(self,_name,_age,_grade,_is_failing):
        self.name = _name
        self.age = _age
        self.grade = _grade
        self.is_failing = _is_failing

    def get_name(self):
            
        return self.name
        
    def get_age(self):

        return self.age
        
    def get_grade(self):

        return self.grade
        
    def get_is_failing(self):

        return self.is_failing

    def set_name(self,new_name):

        self.name = new_name

    def set_age(self, new_age):
        if new_age > 0:
            self.age = new_age

    def set_grade(self,new_grade):

        self.grade = new_grade
    
    def set_is_failing(self,new_is_failing):

        self.is_failing = new_is_failing

    def grade_calc(self, list_of_grades):

        total = 0

        for num in list_of_grades:

            total += num
        
        average = total / len(list_of_grades)

        self.grade = average 

    def __str__(self):
        return (f'name: {self.name}, age: {self.age}, grade: {self.grade}, are you failing: {self.is_failing}.')


list_of_grades = [1,2,3,4,3,4,34,234,1]


student1 = Student('Julissa',22, 89.1,False)

print(student1)

student1.set_age(0)

print(student1)

student1.get_age()
