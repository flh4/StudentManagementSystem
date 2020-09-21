from student import Student

s1 = Student("Jon Doe")
f = s1.getFullName()
print(f)

s1.addGrade('HW', (1,90))
s1.addGrade('tests', (1, 85))

grades2 = s1.getGrades('HW')
print(grades2)
