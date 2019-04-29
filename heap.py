import numpy as np
import time

def heapify(arr, n, i): 
    largest = i
    left = 2 * i
    right = 2 * i + 1
  
    if left < n and arr[i] < arr[left]: 
        largest = left
  
    if right < n and arr[largest] < arr[right]: 
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapifyMin(arr, n, i): 
    smallest = i
    left = 2 * i
    right = 2 * i + 1
  
    if left < n and arr[i] > arr[left]: 
        smallest = left
  
    if right < n and arr[smallest] > arr[right]: 
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapifyMin(arr, n, smallest)


def heapSort(arr): 
    n = len(arr) 

    for i in range(n, -1, -1): 
        heapifyMin(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapifyMin(arr, i, 0) 

arr = [12, 11, 13, 50, 6, 7, -3]
start_time = time.time()

# arr = np.random.randint(1,101,1000000)
heapSort(arr)
print("--- %s seconds ---" % (time.time() - start_time))
n = len(arr)
# for i in range(n): 
# 	print ("%d" %arr[i]), 

for i in range(n - 1, -1, -1):
    print ("%d" %arr[i]),