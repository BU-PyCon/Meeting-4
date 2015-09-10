from ClassRoster import *

math = ClassRoster('Math')
s1 = Student('Butters', 'Math')
s2 = Student('Kyle', 'Math')
s3 = Student('Stan', 'Math')

math.printRoster()

math.addStudent(s1)
math.addStudent(s2)
math.addStudent(s3)

s1.addGrade(100)
s1.addGrade(98)
s1.addGrade(97)
s1.addGrade(86)

s2.addGrade(80)
s2.addGrade(75)
s2.addGrade(64)
s2.addGrade(83)

s3.addGrade(100)
s3.addGrade(100)
s3.addGrade(100)
s3.addGrade(100)

math.printRoster()
math.printGrades()
