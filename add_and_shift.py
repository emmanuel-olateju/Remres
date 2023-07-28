from collections import deque

def add_and_shift(arr, value, size):
    # Append the new value to the end of the deque
    arr.append(value)

    # If the deque size exceeds the desired length, remove the leftmost (oldest) element
    if len(arr) > size:
        arr.popleft()

    return arr