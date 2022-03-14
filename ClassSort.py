import helperFunctions

def sortSchedule(classList):
    n = len(classList)
    classWorkSort(classList, 0, n-1)
    classList.reverse()

    return classList

def classPartition(classList, low, high): 
    i = (low-1) #index of smaller element
    pivot = classList[high].cat

    for j in range(low, high):
        #if current element is smaller than or equal to pivot
        if classList[j].cat <= pivot:
            #increment index of smaller element
            i = i+1
            classList[i], classList[j] = classList[j], classList[i] #if this syntax doesn't work, use placeholder variable

    classList[i+1], classList[high] = classList[high], classList[i+1]
    
    return (i+1)

#implement quicksort to sort classes by class number from least to highest (will reverse output in sortClasses function)
def classWorkSort(classList, low, high):
    if len(classList) == 1:
        return classList
    if low < high:
        #seting partitioning index
        pi = classPartition(classList, low, high)

        #sort elements before and after the partition
        classWorkSort(classList, low, pi-1)
        classWorkSort(classList, pi+1, high)
