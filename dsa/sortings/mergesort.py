from array import *

def merge(arr, low, mid, high):
    global B  # Use global B array
    i = low
    j = mid + 1
    k = low  # Track index in B

    # Merge two sorted subarrays
    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            B[k] = arr[i]
            i += 1
        else:
            B[k] = arr[j]
            j += 1
        k += 1

    # Copy remaining elements from left half
    while i <= mid:
        B[k] = arr[i]
        i += 1
        k += 1

    # Copy remaining elements from right half
    while j <= high:
        B[k] = arr[j]
        j += 1
        k += 1

    # Copy merged elements back to original array
    for x in range(low, high + 1):
        arr[x] = B[x]


def mergesort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        mergesort(arr, low, mid)
        mergesort(arr, mid + 1, high)
        merge(arr, low, mid, high)


# Read input
n = int(input("Enter the size: "))
arr = array('i', [])
B = array('i', [0] * n)  # ✅ Initialize B with the same size as arr

for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))

# Perform merge sort
mergesort(arr, 0, n - 1)

# Print sorted array
print("Sorted array:", list(arr))
