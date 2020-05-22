def func(arr, n):
    i = n - 1
    while i >= 1:
        max1 = 0
        max2 = 0
        for j in (1, i):
            if arr[j] > arr[max1]:
                max2 = max1
                max1 = j
            elif arr[j] > arr[max2]:
                max2 = j
        swap(arr, max1, i)
        swap(arr, max2, i - 1)
        i = i - 2


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


array = [2, 5, 4, 9, 1]
func(array, 5)
print(array)
