import math
from Student import *


class ClassRoster(object):

    def __init__(self, className):
        self.className = className
        self.roster = []

    def printRoster(self):
        if self.__areThereStudents():
            print('The', self.className, 'class has the following',len(self.roster),'student(s):\n')
            for student in self.roster:
                print(student.name)
            print('')

    def printClass(self):
        print('This is the roster for the', self.className, 'class.')

    def printGrades(self):
        if self.__areThereStudents():
            print("The following are all the students' grades for this class:")
            avgGrades = []
            for student in self.roster:
                print('')
                student.printInfo()
                if not math.isnan(student.getAvgGrade()):
                    avgGrades.append(student.getAvgGrade())
            print("\nThe class' average grade is:",sum(avgGrades)/len(self.roster))
            print('')
    
    def addStudent(self, student):
        if self.className == student.className:
            self.roster.append(student)
        else:
            raise Exception('Student is not in this class!')

    def __areThereStudents(self):
        if len(self.roster) > 0:
            return True
        else:
            print('There are currently no students in this', self.className, 'class.\n')
            return False
        
