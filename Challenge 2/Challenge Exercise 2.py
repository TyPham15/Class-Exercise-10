#Challenge Exercise 2
class person:
	def __init__(self, name, age, address, city, state, zipcode):
		self.name = name
		self.age = age
		self.address = address
		self.city = city
		self.state = state
		self.zipcode = zipcode

class Student(person):
	def __init__(self, name, age, address, city, state, zipcode, studentID, GPA):

		super().__init__(name, age, address, city, state, zipcode)

		self.studentID = studentID
		self.GPA = GPA

class Teacher(person):
	def __init__(self, name, age, address, city, state, zipcode, TeacherID, ClassTeaching):

		super().__init__(name, age, address, city, state, zipcode)

		self.TeacherID = TeacherID
		self.ClassTeaching = ClassTeaching


student = Student('Jane Doe', 25, '9 St', 'Santa Ana', 'CA', 12345, 777, 3.8)
print("Student Name: ", student.name)
print("Student Age: ", student.age)
print("Student ID: ", student.studentID)
print("Student GPA: ", student.GPA)
print("Student Address: ", student.address)
print("Student City: ", student.city)
print("Student State: ", student.state)
print("Student Zip code: ", student.zipcode)

print("\n")

teacher = Teacher("Ms. Cantor", 45, '25 St', 'Santa Ana', 'CA', 54321, 7, "Python")
print("Teacher Name: ", teacher.name)
print("Teacher Age: ", teacher.age)
print("Teacher ID: ", teacher.TeacherID)
print("Teacher Course: ", teacher.ClassTeaching)
print("Teacher Address: ", teacher.address)
print("Teacher City: ", teacher.city)
print("Teacher State: ", teacher.state)
print("Teacher Zip code: ", teacher.zipcode)