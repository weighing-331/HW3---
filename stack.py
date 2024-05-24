def quick_sort(arr):
    stack = [(0, len(arr) - 1)]
    while stack:
        start, end = stack.pop()
        if start >= end:
            continue
        pivot = arr[start]
        left, right = start + 1, end
        while left <= right:
            while left <= right and arr[left] <= pivot:
                left += 1
            while left <= right and arr[right] > pivot:
                right -= 1
            if left < right:
                arr[left], arr[right] = arr[right], arr[left]
                print(arr)  # Print the sorting process
        arr[start], arr[right] = arr[right], arr[start]
        stack.append((start, right - 1))
        stack.append((right + 1, end))
        print(arr)  # Print the state of array after partitioning
    return arr

arr = [33, 67, 8, 13, 54, 119, 3, 84, 25, 41]
print("Original array:")
print(arr)
print("Sorting process:")
sorted_arr = quick_sort(arr)
print("Sorted array:")
print(sorted_arr)
