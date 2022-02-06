import csv

#Reading in csv data to two lists and returning them
def readData():
    with open('students.csv', newline='') as studentIn:
        readInStudent = csv.reader(studentIn)
        studentData = list(readInStudent)

    with open('schedule.csv', newline='') as scheduleIn:
        readInSchedule = csv.reader(scheduleIn)
        scheduleData = list(readInSchedule)
    
    return studentData, scheduleData

#Sorting will be done least to most flexible
#This will be done by counting the total number of "X" in the final 21 slots of each student's information
#Those with the most X's will be further down in the list
def sortStudent():
    
    return

#Sorting will be done hardest to easiest class
#This will be done by putting classes in reverse order from how they were read in
def sortSchedule():

    return

def matchingAlg():
    #initialize all students with no class taken & all classes with no student
    #while there are still open classes{
        #class matches with a student
        #if student selected time slot matches
            #if student is not assigned
                #assign student to class
            #else student is already assigned to a class
                #if student 2 is less flexible than student 1
                    #free student 1
                    #assign student 2
                #else student 1 is already least flexible
                    #keep student 1 assigned
        #else select next student
    # }
    return #tentative matching list

#Do later: properly assign the return data to lists
studentData, scheduleData = readData

#Testing print statements to make sure data was loaded correctly
print(studentData)
print(scheduleData)