def sort_single_loop(arr):
    n = len(arr)
    i = 0
    while i < n - 1:
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            i=0  # Reset to start over if any swap is made
        else:
            i += 1

numbers = [4, 2, 9, 1, 5, 6]
sort_single_loop(numbers)
print(numbers)
