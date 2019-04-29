import numpy as np
import time

def merge(arr):
    if len(arr) > 1:
        middle = len(arr)//2
        leftArr = arr[:middle]
        rightArr = arr[middle:]
        merge(leftArr)
        merge(rightArr)
        leftCount, rightCount, resCount = 0, 0, 0
        while leftCount < len(leftArr) and rightCount < len(rightArr):
            if leftArr[leftCount] < rightArr[rightCount]:
                arr[resCount]=leftArr[leftCount]
                leftCount += 1
            else:
                arr[resCount]=rightArr[rightCount]
                rightCount += 1
            resCount += 1

        while leftCount < len(leftArr):
            arr[resCount]=leftArr[leftCount]
            leftCount += 1
            resCount += 1

        while rightCount < len(rightArr):
            arr[resCount]=rightArr[rightCount]
            rightCount += 1
            resCount += 1

def printArr(arr): 
    for i in range(len(arr)):         
        print(arr[i], end=" ")
    print()

start_time = time.time()

arr = np.random.randint(1,101,10000000)
# arr = [54,26,93,17,77,31,44,55,20]
merge(arr)

print("--- %s seconds ---" % (time.time() - start_time))
# printArr(arr)
