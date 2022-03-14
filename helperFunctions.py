import csv
import StudentSort
import ClassSort
import time

Dict = {'102': 0, '105': 1, '107': 2, '109': 3, '110': 4, '111': 5, '112': 6, 
        '301': 7, '302': 8, '311': 9, '312': 10, '361': 11, '362': 12, '380': 13,
        '420': 14, '427': 15, '430': 16, '440': 17, '467': 18, '470': 19, '480': 20}

DictTimes = {'8:00AM': '0', '9:00AM': '1', '10:00AM': '2', '11:00AM': '3', '12:00PM': '4', '1:00PM': '5',
        '2:00PM': '6', '3:00PM': '7'}
        
class Student(list):
    def __init__(self,list):
        self.first = list[0]
        self.last = list[1]
        self.ID = list[2]
        self.email = list[3]

        if(list[4] == "Winter"):
            self.QTR = 1
        if(list[4] == "Spring"):
            self.QTR = 2
        if(list[4] == "Summer"):
            self.QTR = 3
        if(list[4] == "Fall"):
            self.QTR = 4

        self.year = list[5]
        self.applying = list[6]

        if(list[7] == "Yes"):
            self.inEburg = "EBURG"
        else:
            self.inEburg = "WEB"
            
        self.timeslot = []
        for i in range(32):
            if(list[i+8] == "Open"):
                self.timeslot.append(True)
            else:
                self.timeslot.append(False)

        self.pyexp = list[40]
        self.vbexp = list[41]

        self.classesTaken = []
        self.numClassesTaken = 0
        for i in range(21):
            if(list[i+42] == "X"):
                self.classesTaken.append(True)
                self.numClassesTaken += 1
            else:
                self.classesTaken.append(False)

        self.quartersTilGrad = 0

class Schedule(list):
    def __init__(self,list):
        self.sub = list[0]
        self.cat = list[1]
        self.sec = list[2]
        self.title = list[3]
        self.name = list[4]
        self.days = list[5]
        self.timeS = list[6]
        self.timeE = list[7]
        self.location = list[8]
        self.campus = list[9]

#Reading in csv data to two lists and returning them
def readStudentData(student_filename):
    studentData = []
    with open(student_filename, newline='') as studentIn:
        readInStudent = csv.reader(studentIn)
        studentData = list(readInStudent)

    return studentData

def readScheduleData(schedule_filename):
    with open(schedule_filename, newline='') as scheduleIn:
        readInSchedule = csv.reader(scheduleIn)
        scheduleData = list(readInSchedule)
    
    return scheduleData

#Creating class objects using read in data
def createStudentClasses(listOfStudents):
    student_list = []
    for a in range(2,len(listOfStudents)):
        student_list.append(Student(listOfStudents[a]))
    return student_list

def createScheduleClasses(listOfClasses):
    class_list = []
    for a in range(1,len(listOfClasses)):
        class_list.append(Schedule(listOfClasses[a]))
    return class_list

def matchingAlg(student_list, class_list):
    StudentAssigned = [len(student_list)]
    ClassAssigned = [len(class_list)]
    for a in range(len(student_list)):
        StudentAssigned.append(False)
    for i in range(len(ClassAssigned)):
        print(i)
        numAssigned = 0
        tempID = []
        print(len(StudentAssigned))
        if(Dict.get(class_list[i].cat) is not None):
            while numAssigned < 2:
                time.sleep(1)
                print("in while loop")
                for j in range(len(student_list)-1):
                    if(StudentAssigned[j] == False):
                        print("student is not assigned a class")
                        if(student_list[j].classesTaken[Dict.get(class_list[i].cat)] == "True"):
                            print("student has taken the class")
                            if(student_list[j].inEburg == class_list[i].campus):
                                #Check time slots
                                print("student matched")
                                StudentAssigned[j] = True
                                tempID[numAssigned] = student_list[i].ID
                                numAssigned += 1
                            else:
                                continue
                        else:
                            continue
                    else:
                        continue
        ClassAssigned.append("No TA")
    ClassAssigned.append(tuple(tempID[0], tempID[1]))
    return ClassAssigned

#function that calculates the number of quarters until a student graduates based on their graduation quarter and year, using the selected current quarter and year
def getQuartersTilGrad(student, currYrStr, currQrtStr):
    currYr = int(currYrStr.get())

    if((currQrtStr.get()) == "Winter"):
        currQrt = 1
    if((currQrtStr.get()) == "Spring"):
        currQrt = 2
    if((currQrtStr.get()) == "Summer"):
        currQrt = 3
    if((currQrtStr.get()) == "Fall"):
        currQrt = 4
    
    yearsTilGrad = int(student.year) - currYr

    #it does not make sense that you would be generating a schedule for someone who already graduated, but since
    #the input data is randomized, this happens. Because this would never happen in a practical situation, we just set quartersTilGrad to 0
    if yearsTilGrad == 0 and student.QTR < currQrt:
        student.quartersTilGrad = 0
    else:
        student.quartersTilGrad = student.QTR - currQrt
        student.quartersTilGrad = student.quartersTilGrad + (yearsTilGrad*4)

        #if the student has 3 or fewer quarters to graduate and theya re applying for 392, student is bumped up 1 quarter on priority (quartersTilGrad -=1)
        if student.quartersTilGrad <= 3 and student.quartersTilGrad > 0 and student.applying == 392:
            student.quartersTilGrad -=1  


def checkMatchingClass(student, schedule):
    daysList = schedule.days.split(" ")

    for i in range(len(daysList)):
        if(daysList[i] == 'M'):
            return student.timeslot[(0)+dict(schedule.timeS)]
        elif(daysList[i] == 'T'):
            return student.timeslot[(8)+dict(schedule.timeS)]
        elif(daysList[i] == 'W'):
            return student.timeslot[(16)+dict(schedule.timeS)]
        elif(daysList[i] == 'TH'):
            return student.timeslot[(24)+dict(schedule.timeS)]
        else:
            return True