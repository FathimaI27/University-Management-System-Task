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


class Professor(Person):
        def __init__(self,name,age,gender,staff_id,department,salary):
             super().__init__(name,age,gender)
             self.staff_id = staff_id
             self.department = department
             self.salary = salary 
        def set_details(self,staff_id,department,salary):
            self.staff_id = staff_id
            self.department = department
            self.salary = salary 

        def give_feedback(self,student,feedback_string):
              print(f"Feedback for {student.name}: {feedback_string}")

        def increase_salary(self,percentage):
              percentage = percentage/100
              self.salary += self.salary *percentage

        def get_profssor_summary(self):
              print(f"Name: {self.name} age: {self.age} gender: {self.gender} staff_id: {self.staff_id} department: {self.department} salary: {self.salary}")


class Administrator(Person):
    def __init__(self,name,age,gender,admin_id,office,years_of_service):
          super().__init__(name,age,gender)
          self.admin_id = admin_id
          self.office = office
          self.years_of_service = years_of_service
    
    def set_admin_details(self,admin_id,office,years_of_service):
          self.admin_id = admin_id
          self.office = office
          self.years_of_service = years_of_service

    def incrment_service_years(self):
          self.years_of_service += 1 

    def get_admint_summary(self):
          print(f"Name: {self.name} age: {self.age} gender: {self.gender} admin id: {self.admin_id} office: {self.office} years of service : {self.years_of_service}")
          
                
               
              
    
FATHIMA = Student("Fathima",14,"Female",453,"Chemisty")
Christy = Student("Christy,",14,"Female",252,"Chemisty")
Student.add_grade(FATHIMA,40)
Student.add_grade(FATHIMA,60)
print(Student.calculate_average_grades(FATHIMA))
teacher = Professor("BOB","14","Male","4852","Mathematics",1000)
teacher.give_feedback(Christy,"well done")
teacher.increase_salary(50)
Professor.get_profssor_summary(teacher)



    
             
      

