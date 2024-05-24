# HW3

# code.py
## code
```
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

```
## 執行結果
<img width="302" alt="image" src="https://github.com/weighing-331/HW3_quick-sort/assets/68834074/d8b52925-99c1-4aac-8dc0-c43e6bc1a8e5">


# stack.py
## code
```
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

```
## 執行結果
<img width="221" alt="image" src="https://github.com/weighing-331/HW3_quick-sort/assets/68834074/05a0d960-8698-45cf-a3a5-129e434dc617">

# anime.py
## code
```
import matplotlib.pyplot as plt
import matplotlib.animation as animation

states = []

def quick_sort(arr, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= right and arr[left] <= arr[pivot]:
            left += 1
            states.append((arr.copy(), pivot, left, right))
        while left <= right and arr[right] > arr[pivot]:
            right -= 1
            states.append((arr.copy(), pivot, left, right))
        if left < right: #swapped
            arr[left], arr[right] = arr[right], arr[left]
            states.append((arr.copy(), pivot, left, right))

    arr[pivot], arr[right] = arr[right], arr[pivot]
    states.append((arr.copy(), pivot, left, right)) 

    quick_sort(arr, start, right - 1) # 排左
    quick_sort(arr, right + 1, end) # 排右

# 初始
arr = [33, 67, 8, 13, 54, 119, 3, 84, 25, 41]
initial_array = arr.copy()
print("Original array:")
print(arr)

# 開始排序
quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:")
print(arr)

# 動畫
fig, ax = plt.subplots()
bar_rects = ax.bar(range(len(arr)), arr, align="edge")
ax.set_xlim(0, len(arr))
ax.set_ylim(0, max(arr) * 1.1)
iteration = [0]


text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
label = [ax.text(i, val, str(val), ha='center', va='bottom') for i, val in enumerate(arr)]

pivot_text = ax.text(0, 0, "", color="red", ha="center")
left_text = ax.text(0, 0, "", color="blue", ha="center")
right_text = ax.text(0, 0, "", color="green", ha="center")


def init():
    for rect, val, lbl in zip(bar_rects, initial_array, label):
        rect.set_height(val)
        lbl.set_position((rect.get_x() + rect.get_width() / 2, val))
        lbl.set_text(val)
    text.set_text("Initial array")
    pivot_text.set_text("")
    left_text.set_text("")
    right_text.set_text("")
    return bar_rects, label, text, pivot_text, left_text, right_text

def update_fig(state, rects, iteration, label, pivot_text, left_text, right_text):
    arr, pivot, left, right = state
    for rect, val, lbl in zip(rects, arr, label):
        rect.set_height(val)
        lbl.set_position((rect.get_x() + rect.get_width() / 2, val))
        lbl.set_text(val)

    pivot_text.set_position((pivot, arr[pivot] * 1.05))
    pivot_text.set_text(f"Pivot\n{arr[pivot]}")

    if left < len(arr):
        left_text.set_position((left, arr[left] * 1.05 if left < len(arr) else 0))
        left_text.set_text(f"Left\n{arr[left] if left < len(arr) else ''}")

    if right >= 0:
        right_text.set_position((right, arr[right] * 1.05 if right >= 0 else 0))
        right_text.set_text(f"Right\n{arr[right] if right >= 0 else ''}")

    iteration[0] += 1
    text.set_text(f"Iteration: {iteration[0]}")

anim = animation.FuncAnimation(
    fig, update_fig, frames=states, init_func=init, fargs=(bar_rects, iteration, label, pivot_text, left_text, right_text), interval=500, repeat=False
)

plt.show()

```
## 執行結果
動畫模擬排序過程
![Figure_1](https://github.com/weighing-331/HW3_quick-sort/assets/68834074/5c569202-9e2e-446f-a3ab-123050afecfa)
![anime](https://github.com/weighing-331/HW3_quick-sort/assets/68834074/69e15e3b-8f15-4ff4-9508-c89fee087549)


