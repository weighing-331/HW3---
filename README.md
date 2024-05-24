# HW3
``
def quick_sort(arr, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= right and arr[left] <= arr[pivot]:
            left += 1
        while left <= right and arr[right] > arr[pivot]:
            right -= 1
        if left < right: #swapped
            arr[left], arr[right] = arr[right], arr[left]
            print(f"Swapped: {arr}")

    arr[pivot], arr[right] = arr[right], arr[pivot]
    print(f"Swapped pivot: {arr}")

    quick_sort(arr, start, right - 1) # 排左
    quick_sort(arr, right + 1, end) # 排右

arr = [33, 67, 8, 13, 54, 119, 3, 84, 25, 41]
print("Original array:")
print(arr)
print("Sorting process:")
quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:")
print(arr)

``
