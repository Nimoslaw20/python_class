class Student:                                                     #Instances for students include: name, gender, GPA, Accomodation, course
    def __init__(self, Name, gender, GPA, acc, Course):
        self.Name = Name
        self.gender = gender
        self.GPA = GPA
        self.acc = acc
        self.Course = Course
        self.stList = [ ]

  #Accessor methods
        
    def getName(self):
        return self.Name

    def getCourse(self):
        return self.Course

    def getGPA(self):
        return self.GPA

    def getAcc(self):
        return self.acc


    #Mutator  methods
    def setName(self, newName):                    #Mutating name
        self.Name = newName

    def setCourse(self, newCourse):                #Mutating course
        self.Course = newCourse

    def setGPA(self, newGPA):                  # Mutating GPA
        self.GPA = newGPA

    def setAcc(self, newacc):
        self.acc = newacc


#other methods
    def sAdd(self, name):       # A method for adding students
        return self.stList.append(name)
    

    def sDrop(self, name):       #A method for dropping students
        self.stList.remove(name)

    def sCount(self, name):      # Count the number of students
        return (len(self.stList ))

    def sList(self, course):
        a = ' '
        for i in self.stList:
            a += i + ' , '
        return a
        
   
    def StudInfo(self):
        return '{0:20} {1:^15} {2:^10.2f} {3:^30} {4:^40}'.format(self.Name, self.gender, self.GPA, self.acc, self.Course)
