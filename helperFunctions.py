import csv
import StudentSort
import ClassSort

Dict = {102: '0', 105: '1', 107: '2', 109: '3', 110: '4', 111: '5', 112: '6', 
        184: '7', 301: '8', 302: '9', 311: '10', 312: '11', 325: '12', 361: '13', 362: '14', 
        380: '15', 392: '16', 420: '17', 427: '18', 430: '19', 440: '20', 470: '21', 
        480: '22', 481: '23', 489: '24', 492: '25'}
        
class Student(list):
    first = list[0]
    last = list[1]
    ID = list[2]
    email = list[3]
    QTR = list[4]
    year = list[5]
    applying = list[6]
    inEburg = list[7]
    timeslot = []
    for i in range(32):
        timeslot.append(list[8+i])
    pyexp = list[40]
    vbexp = list[41]
    classesTaken = []
    for i in range(25):
        classesTaken.append(list[42+i])
    numClassesTaken = len(classesTaken)
    quartersTilGrad = 0

class Schedule(list):
    sub = list[0]
    cat = list[1]
    sec = list[2]
    title = list[3]
    name = list[4]
    days = list[5]
    timeS = list[6]
    timeE = list[7]
    location = list[8]
    campus = list[9]

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

def createStudentClasses(listOfStudents):
    a = 2
    student_list = []
    for a in range(len(listOfStudents)):
        temp = Student(listOfStudents[a])
        print(a)
        student_list[a-2].append(temp)
    return student_list

def createScheduleClasses(listOfClasses):
    a = 1
    class_list = []
    for a in range(len(listOfClasses)):
        temp = Schedule(listOfClasses[a])
        class_list[a-1].append(temp)
    return class_list

def matchingAlg(student_list, class_list):
    StudentAssigned = [len(student_list)]
    ClassAssigned = [len(class_list)]
    for a in range(len(StudentAssigned)):
        StudentAssigned[a] = False
    for i in range(len(ClassAssigned)):
        numAssigned = 0
        tempID = []
        while numAssigned < 2:
            for j in range(len(student_list)):
                if StudentAssigned[j] == False:
                    if student_list[j].classesTaken[dict(class_list[i].cat)] == "X":
                        #Check campus compatibility
                            #Check time slots
                                StudentAssigned[j] = True
                                tempID[numAssigned] = student_list[i].ID
                                numAssigned += 1
                else:
                    continue
        ClassAssigned[i] = (tempID[0], tempID[1])
    return ClassAssigned