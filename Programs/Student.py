class Student:

    def __init__(self, name, className):
        self.name = name
        self.className = className
        self.testGrades = []

    def printInfo(self):
        print('The student ', self.name, ', in the class ', self.className,
              ', has the following grades:\n', sep = '')
        if len(self.testGrades) == 0:
            print('No available grades.\n')
            print('Average Grade: N/A')
        else:
            for i,v in enumerate(self.testGrades):
                print(v, end = '')
                if i != len(self.testGrades)-1:
                    print(', ', end = '', sep = '')
            print('\n')
            print('Average Grade: ', self.getAvgGrade())

    def getAvgGrade(self):
        if len(self.testGrades) > 0:
            return sum(self.testGrades)/len(self.testGrades)
        else:
            return float('nan')
    
    def addGrade(self, grade):
        if isinstance(grade, int):
            if 0 <= grade <= 100:
                self.testGrades.append(grade)
            else:
                errorStr = 'Inappropriate value for a grade. Should be between [0,100]. The value '+str(grade)+' was given instead.'
                raise ValueError(errorStr)
        else:
            errorStr = 'Incorrect variable type for a grade. Should be an int. The type '+type(grade).__name__+' was given instead.'
            raise TypeError(errorStr)
