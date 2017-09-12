from stu import Student
from inst import Instructor
class Universityclass(list):

    def __init__(self, name, ID, course, dpt, inst):  # Name, ID, Course, Department, Instructor
        self.name = name
        self.ID = ID
        self.dpt = dpt
        self.inst= inst
        self.course = course
        self.Newlist = [ ]
        

#Accessor methods for getting name, ID, Department, Instructor, Course
        
    def getName(self):
        return self.name

    def getID(self):
        return self.ID

    def getDpt(self):
        return self.dpt

    def getInst(self):
        return self.inst
    
    def getCourse(self):
        return self.course


#Mutator  methods for setting name, ID, Course, Department
    def setName(self, newname): 
        self.name = newname

    def setID(self, newID):
        self.ID = newID

    def setCourse(self, newCourse):
        self.course = newCourse

    def setDpt(self, newDpt):
        self.dpt = newDpt

    def setInst(self, newIn):
        self.inst= newIn
    
    def details(self):
        return '{} {} {} {} {}'.format(self.name, self.ID, self.course, self.dpt, self.inst)

    def StudentAdd(self, name):
        return self.Newlist.append(name)
    

    def StudentDrop(self, name):                       # Drop a student
        self.Newlist.remove(name)

    def StudentCount(self, name):                      # Count the students in the list
        return (len(self.Newlist))

    def LStudent(self, course):
        c = ' '
        for i in self.Newlist:
            c += i + ' , '
        return c
        #print(' , '.join(self.Newlist))
        

def main():
              x = Instructor('Andy', 'Calculus', 'Monday', 45)
              x_1 = Universityclass('Andy', 453, 'DS', 'ENG', x)                 # Details of the UniversityClass
              print(Universityclass.details(x_1))   

              print('The person just registered for  Data Structure:', x_1.getName())
              print('His ID is: ', x_1.getID(),  'and his instructor is ', x_1.getInst())
              print('The course registered for is: ', x_1.getCourse())
              x_1.setName('Permish')
              print(x_1.getName(), 'just registered for Data Structures')
              print('One student joined the course: Ama', x_1.StudentAdd('Ama'))
              print('One student joined the course: Kojo', x_1.StudentAdd('Kojo'))
              print('One student joined the course: Mac ', x_1.StudentAdd('Mac'))
              print('The number of students currently enrolled in Data Structure is:',  x_1.StudentCount('DS'))
              print('One student dropped out of this course: Ama', x_1.StudentDrop('Ama'))
              print('Hence the currently number of students is: ', x_1.StudentCount('DS'))
              print('And they are',x_1.LStudent('DS'))
              

              print()
              print(('The Student Class Details').upper())                         # Student details
              s = Student('Charlie', 'F', 3.7, 'on-campus', 'Calculus')              #Details for student 1
              y = Student('Yoda','M', 3.6, 'on-campus', 'Calculus')                # Details for Student 2
              print( '{0:20} {1:^15} {2:^10} {3:^30} {4:^40}'.format('Name', 'Gender', 'GPA', 'Accommodation', 'Course'))

              print(Student.StudInfo(s))
              print(Student.StudInfo(y))
              print()
              print(('other details').upper())

    
              print('The name of the Ashesi Student:', s.getName())
              print('The person offers', s.getCourse(), 'and his ', s.getGPA(), 'GPA.')
              print('The student residence is', s.getAcc())

              s.sAdd('Randy')                                          #James was added to the instructor list
              s.sAdd('Bright')                                          #Kwame was added to the instructor list
              print('The following students were added to do', s.getCourse(), ':',  s.sList('Calculus'))
              print('The number students added is', s.sCount('Calculus'))
              s.sDrop('Bright')                                        # Bright drops
              print('The remaining number of added students is ', s.sCount('Calculus'))
              s.setName('Roy')                                       # Roy replaces Charles
              print(s.getName(), 'replaces Charlie')
              s.setGPA(3.90)
              print('His GPA is now: ', s.getGPA())

              print()                             #Print a space
              print(('the Instructor class details').upper())
              
              print('{0:15} {1:10} {2:15} {3:15}'.format('Name', 'Course', 'Day', 'Number of Students'))
              print(Instructor.InstInfo(x))
                
                
              print()
              print(('a few descriptions of the lecturer').upper())
              print('The name of the instructor for this class is', x.getname())
              print('The lecturer teaches', x.getcourse(), 'on',  x.getDay())
              print('The number of students in', x.getcourse(), 'is', x.getNum())

              x.InstAdd('James')                                          #James was added to the instructor list
              x.InstAdd('Kwame')                                          #Kwame was added to the instructor list
              print('Faculty interns for', x.getcourse(), 'are',  x.InstructorList('Calculus'))
              print('The number of instructors added is', x.InstCount('Calculus'))
              print('You can reach the instructor on this email: ', x.Instmail())
              print('Find the general information about the lecturer:', x.InstInfo())
             

                

                

if __name__ == '__main__':
          main()

