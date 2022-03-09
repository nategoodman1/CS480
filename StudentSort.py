#function that calculates the number of quarters until a student graduates based on their graduation quarter and year, using the selected current quarter and year
def getQuartersTilGrad(student, currYr, currQrt):
    quartersTilGrad = 0
    yearsTilGrad = student.year - currYr
    student.quartersTilGrad = student.quarter - currQrt
    student.quartersTilGrad = student.quartersTilGrad + (yearsTilGrad*4)

    #if the student has 3 or fewer quarters to graduate and they are applying for 392, student is bumped up 1 quarter on priority (quartersTilGrad -=1)
    if student.quartersTilGrad <= 3 and student.applying == 392:
        student.quartersTilGrad -= 1
    

#main student sort function
def sortStudents(studentList):
    n = len(studentList)
    classesTakenSort(classSelectionSort(gradQrtSort(studentList, 0, n)))
    
    return studentList

#partition for quarters until graduation sort
def gradQrtPartition(studentList, low, high): 
    i = (low-1) #index of smaller element
    pivot = studentList[high].quartersTilGrad

    for j in range(low, high):
        #if current element is smaller than or equal to pivot
        if studentList[j].quartersTilGrad <= pivot:
            #increment index of smaller element
            i = i+1
            studentList[i], studentList[j] = studentList[j], studentList[i] #if this syntax doesn't work, use placeholder variable

    studentList[i+1], studentList[high] = studentList[high], studentList[i+1]
    
    return (i+1)

#implement quicksort to sort students by quarters until graduation from least to highest
def gradQrtSort(studentList, low, high):
    if len(studentList) == 1:
        return studentList
    if low < high:
        #seting partitioning index
        pi = gradQrtPartition(studentList, low, high)

        #sort elements before and after the partition
        gradQrtSort(studentList, low, pi-1)
        gradQrtSort(studentList, pi+1, high)

#partition for class application sort (392 vs 492)
def selectionPartition(studentList, low, high): 
    i = (low-1) #index of smaller element
    pivot = studentList[high].apply

    for j in range(low, high):
        #if current element is smaller than or equal to pivot
        if studentList[j].apply <= pivot:
            #increment index of smaller element
            i = i+1
            studentList[i], studentList[j] = studentList[j], studentList[i] #if this syntax doesn't work, use placeholder variable

    studentList[i+1], studentList[high] = studentList[high], studentList[i+1]
    
    return (i+1)

#implement quicksort to sort students by class applying for (392 is first in this sort, so we will need to reverse this output)
def selectionWorkSort(studentList, low, high):
    if len(studentList) == 1:
        return studentList
    if low < high:
        #seting partitioning index
        pi = selectionPartition(studentList, low, high)

        #sort elements before and after the partition
        selectionWorkSort(studentList, low, pi-1)
        selectionWorkSort(studentList, pi+1, high)

#sort that takes in list sorted by graduation quarter, where for every value of quartersUntilGraduation, the sublists are sorted by class applying for (492 vs 392)
def classSelectionSort(studentList):
    workList = []
    outList = []

    while(len(studentList) > 0):
        #if students 0 and 1 are both graduating in the same quarter, add student 0 to workList and remove it from studentList, then restart loop
        if studentList[0].quartersTilGrad == studentList[1].quartersTilGrad:
            workList.append(studentList[0])
            studentList.pop(0)
            continue
        #if students 0 and 1 are not graduating in the same quarter, add student 0 to workList and remove it from studentList,
        #sort workList by class application, extend workList to outList, and clear workList
        else:
            workList.append(studentList[0])
            studentList.pop(0)
            n = len(workList)
            selectionWorkSort(workList, 0, n)
            workList.reverse() #reversing output to prioritize 492 over 392
            classesTakenSort(workList)
            outList.extend(workList)
            workList.clear()
    
    studentList.extend(outList)


#partition for the number of classes taken sort
def classesTakenPartition(studentList, low, high): 
    i = (low-1) #index of smaller element
    pivot = studentList[high].numClassesTaken

    for j in range(low, high):
        #if current element is smaller than or equal to pivot
        if studentList[j].numClassesTaken <= pivot:
            #increment index of smaller element
            i = i+1
            studentList[i], studentList[j] = studentList[j], studentList[i] #if this syntax doesn't work, use placeholder variable

    studentList[i+1], studentList[high] = studentList[high], studentList[i+1]

#implement quicksort to sort students by class applying for (392 is first in this sort, so we will need to reverse this output)
def classesTakenWorkSort(studentList, low, high):
    if len(studentList) == 1:
        return studentList
    if low < high:
        #seting partitioning index
        pi = classesTakenPartition(studentList, low, high)

        #sort elements before and after the partition
        classesTakenWorkSort(studentList, low, pi-1)
        classesTakenWorkSort(studentList, pi+1, high)

#function that sorts sublist of students by the number of classes they have taken from lowest to highest
def classesTakenSort(studentList):
    workList = []
    outList = []

    while(len(studentList) > 0):
        #if students 0 and 1 are both applying for same class, add student 0 to workList and remove it from studentList, then restart loop
        if studentList[0].apply == studentList[1].apply:
            workList.append(studentList[0])
            studentList.pop(0)
            continue
        #if students 0 and 1 are not applying for same class, add student 0 to workList and remove it from studentList,
        #sort workList by classes taken, extend workList to outList, and clear workList
        else:
            workList.append(studentList[0])
            studentList.pop(0)
            n = len(workList)
            classesTakenWorkSort(workList, 0, n)
            outList.extend(workList)
            workList.clear()

    studentList.extend(outList)            
