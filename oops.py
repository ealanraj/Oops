# class car:
#     def __init__(self,brand,model,year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#     def __str__(self):
#         return f"Brand = {self.brand}\nModel = {self.model}\nYear = {self.year}"
#     def greet(self):
#         return f"vanakam {self.brand}"

# alan_car = car("BMW","M3",2024)

# print(alan_car)
# alan_car.brand = "Benz"
# print(alan_car)
# print(alan_car)

#Inheritence
class Person: #parent class - base class
  def __init__(self,firstname,lastname):
    self.firstname = firstname
    self.lastname = lastname
  
  def __str__(self):
    return f"{self.firstname} {self.lastname}"

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

rollno_1 = Person('Alan','Raj')
rollno_1.printname()
print(rollno_1)

class Student(Person):#child class - derived class
  def __init__(self,firstname,lastname,school):
    super().__init__(firstname,lastname)
    self.school = school
  def __str__(self):
    return f"fullname = {self.firstname} {self.lastname}\nschool = {self.school}"
  def ln(self):
    print(self.lastname)
  def fn(self):
    print(self.firstname)

rollno_2 = Student("Krishna","Divakar","achariya") 
print(rollno_2)
rollno_2.ln()
rollno_2.fn()