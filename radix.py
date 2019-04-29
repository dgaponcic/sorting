def radix(arr, power):
    length = len(arr)
    res = [0] * (length)
    count = [0] * (10)
    for i in range(0, length):
        index = int(arr[i] / power)
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = length - 1
    while i >= 0:
        index = int(arr[i]/power)
        res[count[(index)%10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
        print(count[index % 10])
        print(res)
        print(count)
        print()
    i = 0
    for i in range(0,len(arr)): 
        arr[i] = res[i]

arr = [1, 3, 6, 2, 50]
max = max(arr)
power = 1
while(int(max / power) > 0):
    radix(arr, power)
    power *= 10
print(arr)