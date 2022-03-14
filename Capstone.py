import helperFunctions
import StudentSort
import ClassSort
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox

root = Tk()
root.title("TA Class Matching")
root.resizable(False,False)
frame = ttk.Frame(root, padding = 20)
frame.grid()

student_filename = StringVar()
classes_filename = StringVar()
output_destination = StringVar()
quarter_name_str = StringVar()
graduation_year_str = StringVar()

def main_function(student_filename, classes_filename):

    studentFN = student_filename.get()
    classesFN = classes_filename.get()
    studentDataList = helperFunctions.readStudentData(studentFN)
    classDataList = helperFunctions.readScheduleData(classesFN)

    student_list = []
    class_list = []
    paired_list = []
    
    #converting list of student data into student objects
    student_list = helperFunctions.createStudentClasses(studentDataList)
    class_list = helperFunctions.createScheduleClasses(classDataList)

    for i in range(len(student_list)):
        helperFunctions.getQuartersTilGrad(student_list[i], graduation_year_str, quarter_name_str)
    
    #Sorting the lists
    sorted_student_list = StudentSort.sortStudents(student_list)
    sorted_class_list = ClassSort.sortSchedule(class_list)
    
    #Matching algorithm
    if (len(sorted_student_list) > 0) and (len(sorted_class_list) > 0):
        paired_list = helperFunctions.matchingAlg(sorted_student_list, sorted_class_list)
    else:
        messagebox.showerror('FileName Error', 'Error: Filename too short. Please verify selected files')

    helperFunctions.CSVWrite(paired_list, sorted_class_list, output_destination)

    messagebox.showinfo('Success!', 'Success! Students and classes matched and file output to selected destination!')
 
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

quarter_name_str.set("Pick a Quarter")
quarter_menu = ttk.OptionMenu(frame, quarter_name_str, "Fall", "Winter", "Spring", "Summer")
quarter_menu.grid(row=3, column = 1)
graduation_year_str.set("Select Graduation Year")
year_menu = ttk.OptionMenu(frame, graduation_year_str, "2022", "2023", "2024", "2025", "2026")
year_menu.grid(row=3,column=2)
ttk.Label(frame, text="Select Current Quarter").grid(row=3, column=0)

ttk.Button(frame, text="Generate Matches", command=lambda: main_function(student_filename, classes_filename)).grid(column=2, row=7)

root.mainloop()