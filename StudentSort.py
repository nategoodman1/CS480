def sortStudents(studentList):
    n = len(studentList)
    gradQrtSort(studentList, 0, n-1)
    classSelectionSort(studentList)

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
            studentList[i], studentList[j] = studentList[j], studentList[i]

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
    pivot = int(studentList[high].applying)

    for j in range(low, high):
        #if current element is smaller than or equal to pivot
        if int(studentList[j].applying) <= pivot:
            #increment index of smaller element
            i = i+1
            studentList[i], studentList[j] = studentList[j], studentList[i]

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
        #if studentList has only one element, add it to the workList, remove it from studentList, sort workList, then extend workList to outList
        if len(studentList) == 1:
            workList.append(studentList[0])
            studentList.pop(0)
            #if there is more than one element in workList, sort workList by classes taken
            if(len(workList) > 1):
                selectionWorkSort(workList, 0, (len(workList)-1))
                #reversing output to prioritize 492 over 392
                workList.reverse()
                #if there is more than one element in workList, sort workList by classes taken
                #classesTakenSort(workList)
            outList.extend(workList)
        #if students 0 and 1 are both graduating in the same quarter, add student 0 to workList and remove it from studentList, then restart loop
        elif studentList[0].quartersTilGrad == studentList[1].quartersTilGrad:
            workList.append(studentList[0])
            studentList.pop(0)
            continue
        #if students 0 and 1 are not graduating in the same quarter, add student 0 to workList and remove it from studentList,
        #sort workList by class application, extend workList to outList, and clear workList
        else:
            workList.append(studentList[0])
            studentList.pop(0)

            #if there is more than one element in workList, sort it. Otherwise, extend it to outList
            if(len(workList) > 1):
                selectionWorkSort(workList, 0, (len(workList)-1))
                #reversing output to prioritize 492 over 392
                workList.reverse()
                #if there is more than one element in workList, sort workList by classes taken
                #classesTakenSort(workList)
            #extend workList to outList. The students in workList should all be graduating within the same quarter 
            #and be sorted by the amount of classes they have taken (lowest to highest)
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
            studentList[i], studentList[j] = studentList[j], studentList[i]

    studentList[i+1], studentList[high] = studentList[high], studentList[i+1]

    return(i+1)

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
        #if there is only one element left in studentList, add it to the workList, then extend workList to outList
        if len(studentList) == 1:
            workList.append(studentList[0])
            studentList.pop(0)
            #if there is more than one element in workList, sort it. Otherwise, extend it to outList
            if(len(workList) > 1):
                classesTakenWorkSort(workList, 0, (len(workList)-1))
            outList.extend(workList)
        #if students 0 and 1 are both applying for same class, add student 0 to workList and remove it from studentList, then restart loop
        elif int(studentList[0].applying) == int(studentList[1].applying):
            workList.append(studentList[0])
            studentList.pop(0)
            continue
        #if students 0 and 1 are not applying for same class, add student 0 to workList and remove it from studentList,
        #sort workList by classes taken, extend workList to outList, and clear workList
        else:
            workList.append(studentList[0])
            studentList.pop(0)

            #if there is more than one element in workList, sort it. Otherwise, extend it to outList
            if(len(workList) > 1):
                classesTakenWorkSort(workList, 0, (len(workList)-1))
            #extend workList to outList. workList should now contain students all applying for the same class sorted by their num of classes taken
            outList.extend(workList)
            workList.clear()
            

    studentList.extend(outList)