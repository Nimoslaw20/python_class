
class  Instructor:
    def __init__(self, name, course, day, number):
        self.name = name
        self.course = course
        self.day = day
        self.num = number
        self.mail = self.name+ '@' +'gmail.com'
        self.InstList = [ ]
        

        #Accessor methods for getting instructor'
        
    def getname(self):
        return self.name

    def getcourse(self):
        return self.course

    def getDay(self):
        return self.day

    def getNum(self):
        return self.num


    #Mutator  methods
    def setName(self, newname): 
        self.name = newname

    def setcourse(self, newcourse):
        self.course = newcourse

    def setDay(self, newDay):
         self.day = newDay

    def setNum(self, newnum):
        self.num = newnum



    def InstAdd(self, name):       # A method for adding instructors
        return self.InstList.append(name)
    

    def Instdrop(self, name):       #A method for dropping instructors
        self.InstList.remove(name)

    def InstCount(self, name):      # Count the number of lecturers in the university
        return (len(self.InstList ))

    def InstructorList(self, course):
        a = ' '
        for i in self.InstList:
            a += i + ' , '
        return a

    def InstInfo(self):
        return '{0:15} {1:10} {2:15} {3:15}'.format(self.name, self.course, self.day, self.num)

    def Instmail(self):
         return self.mail
