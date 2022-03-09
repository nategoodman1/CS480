import csv
import StudentSort
import ClassSort
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox

Dict = {102: '0', 105: '1', 107: '2', 109: '3', 110: '4', 111: '5', 112: '6', 
        184: '7', 301: '8', 302: '9', 311: '10', 312: '11', 325: '12', 361: '13', 362: '14', 
        380: '15', 392: '16', 420: '17', 427: '18', 430: '19', 440: '20', 470: '21', 
        480: '22', 481: '23', 489: '24', 492: '25'}
        
class Student(list):
    first = list[1]
    last = list[2]
    ID = list[3]
    email = list[4]
    QTR = list[5]
    year = list[6]
    applying = list[7]
    inEburg = list[8]
    timeslot = []
    for i in range(32):
        timeslot.append(list[9+i])
    pyexp = list[41]
    vbexp = list[42]
    classesTaken = []
    for i in range(25):
        classesTaken.append(list[43+i])

class Schedule(list):
    sub = list[1]
    cat = list[2]
    sec = list[3]
    title = list[4]
    name = list[5]
    days = list[6]
    timeS = list[7]
    timeE = list[8]
    location = list[9]
    campus = list[10]

#Reading in csv data to two lists and returning them
def readStudentData():
    with open('students.csv', newline='') as studentIn:
        readInStudent = csv.reader(studentIn)
        studentData = list(readInStudent)

    return studentData

def readScheduleData():
    with open('schedule.csv', newline='') as scheduleIn:
        readInSchedule = csv.reader(scheduleIn)
        scheduleData = list(readInSchedule)
    
    return scheduleData

#Sorting will be done least to most flexible
#This will be done by counting the total number of "X" in the final 21 slots of each student's information
#Those with the most X's will be further down in the list
def sortStudent():
    
    return

#Sorting will be done hardest to easiest class
#This will be done by putting classes in reverse order from how they were read in
def sortSchedule():

    return

def matchingAlg(student_list, class_list):
    StudentAssigned = [len(student_list)]
    ClassAssigned = [len(class_list)]
    for a in range(len(StudentAssigned)):
        StudentAssigned[a] = False
    for i in range(len(ClassAssigned)):
        for j in range(len(student_list)):
            if StudentAssigned[j] == False:
                if student_list[j].classesTaken[dict(class_list[i].cat)] == True:
                    #if time slots match up
                        ClassAssigned[i] = student_list[i].ID
            else:
                continue
    return ClassAssigned

#Do later: properly assign the return data to lists
#studentData, scheduleData = readData

root = Tk()
root.title("TA Class Matching")
root.resizable(False,False)
frame = ttk.Frame(root, padding = 20)
frame.grid()

student_filename = StringVar()
classes_filename = StringVar()
output_destination = StringVar()
quarter_name = StringVar()
graduation_year = StringVar()

drop = OptionMenu(root,quarter_name,"Fall","Winter","Spring","Summer")
drop.pack()

def main_function(student_list, class_list):
    
    if (len(student_list) > 0) and (len(class_list) > 0):
        output_destination = matchingAlg(student_list, class_list)
    else:
        messagebox.showerror('FileName Error', 'Error: Filename too short. Please verify selected files')        

def select_studentfile():

    filename = fd.askopenfilename(title="Choose Students csv File", initialdir="/", filetypes=(("csv Files", "*.csv"),))

    student_filename.set(filename)


def select_classesfile():

    filename = fd.askopenfilename(title="Choose Classes csv File", initialdir="/", filetypes=(("csv Files", "*.csv"),))

    classes_filename.set(filename)


def select_output():

    directoryname = fd.askdirectory(title="Choose Directory to Save Output", initialdir="/")

    output_destination.set(directoryname)

ttk.Label(frame, text="Students File:").grid(column=0, row=1)
ttk.Button(frame, text="Choose File", command=select_studentfile).grid(column=1, row=2)
student_entry = Entry(frame, textvariable = student_filename).grid(column=0,row=2)

ttk.Label(frame, text="Classes File:").grid(column=0, row=5)
ttk.Button(frame, text="Choose File", command=select_classesfile).grid(column=1, row=6)
classes_entry = Entry(frame, textvariable = classes_filename).grid(column=0, row=6)

ttk.Label(frame, text="Output Destination:").grid(column=3, row=3)
ttk.Button(frame, text="Choose Folder", command=select_output).grid(column=4, row=4)
output_entry = Entry(frame, textvariable = output_destination).grid(column=3, row=4)

ttk.Button(frame, text="Generate Matches", command=main_function(student_filename, classes_filename)).grid(column=2, row=7)

root.mainloop()