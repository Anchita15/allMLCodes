from student import Student
student1 = Student("Jim", "Business", 3.1, False)
print(student1.name)
print(student1.gpa)
student2 = Student("Pam", "Art", 2.5, True)
print(student2.major)

print(student1.on_honor_roll())