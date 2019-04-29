import numpy as np
import time

def partition_Middle(arr, low, high):
	middle = int((low + high) / 2 - (low + high) % 2)
	if high - low == 1:
		if(arr[low] > arr[high]):
			# print('here')
			arr[low], arr[high] = arr[high], arr[low]
		return high
	pivot = arr[middle]
	right = high
	left = low
	while 1:
		while left < high and arr[left] < pivot:
			left += 1
		while arr[right] > pivot:
			right -= 1
		if(left >= right):
			break
		arr[left], arr[right] = arr[right], arr[left]
		left += 1
		right -= 1
	while left < middle:
		arr[left], arr[middle] = arr[middle], arr[left]
		left += 1
	while right > middle:
		arr[right], arr[middle] = arr[middle], arr[right]
		right -= 1
	return left


def partition_First(arr,low,high): 
    pivot = arr[low]
    i = low 
    for j in range(low + 1, high + 1):
        if  arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i], arr[low] = arr[low], arr[i]
    return i

def partition_Last(arr,low,high): 
    pivot = arr[high]
    i = low - 1
    for j in range(low , high):
        if  arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i] 
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quickSort(arr,low,high): 
	if low < high:
		pi = partition_Middle(arr, low, high)
		# print(pi)
		quickSort(arr, low, pi - 1)
		quickSort(arr, pi, high)
		# print(arr)

arr = [10, 7, 8, 56, -3] 
# arr = [int(i) for i in input().split()]
n = len(arr)
quickSort(arr, 0, n - 1)
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
