def func(arr, n):
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                swap(arr, i, j)

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


array = [2, 5, 4, 9, 1]
func(array, 5)
print(array)