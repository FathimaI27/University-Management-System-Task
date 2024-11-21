class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender


    def set_details(self,name,age,gender):
            self.name = name
            self.age = age
            self.gender = gender

    def get_details(self):
        string = (f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")
        return string


class Student(Person):
        def __init__(self,name,age,gender,student_id,course):
               super().__init__(name,age,gender)
               self.student_id = student_id
               self.course = course
               self.grades = []
        def set_details(self,student_id,course):
               self.student_id = student_id
               self.course = course

        def add_grade(self,grade):
              self.grades.append(grade)

        def calculate_average_grades(self):
             average =  sum(self.grades)/(len(self.grades))
             return average 
        
        def get_student_summary(self):
            print(self.name )
            print(self.age)
            print(self.gender)
            print(self.student_id)
            print(self.course)

      
      
      
               

FATHIMA = Student("Fathima",14,"Female",453,"Chemisty")
Christy = Student("Christy,",14,"Female",252,"Chemisty")
Student.add_grade(FATHIMA,40)
Student.add_grade(FATHIMA,60)
print(Student.calculate_average_grades(FATHIMA))

class Professor(Person):
       def __init__(self,name,age,gender,staff_id,departments,salary):
             super().__init__(name,age,gender)
             self.staff_id = staff_id
             self.departments =departments
             self.salary = salary 
             
      

