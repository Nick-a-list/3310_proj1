import random
import numpy as np

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2 #middle number
    left = merge_sort(arr[:mid]) #left side of array not including mid
    right = merge_sort(arr[mid:]) #right side of array not including mid
    #after recursion, this function returns the return value of merging left and right
    return merge(left, right)

def merge(left, right):
    arr = []
    i = j = 0

    #compares each half of array and builds the sorted array
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            #checks each index from left and right array
            #switches places and increments whose index value is lower
            arr.append(left[i])
            i+=1
        else:
            arr.append(right[j])
            j+=1

    # Append any remaining elements
    arr.extend(left[i:])
    arr.extend(right[j:])

    return arr

def partition(arr, low, high):
    #goal is to pick last element as pivot and places it in correct position
    # Pick a random index between low and high
    rand_index = random.randint(low, high)

    # Swap that random element to the 'high' position
    arr[rand_index], arr[high] = arr[high], arr[rand_index] #this prevents a Recursion Error

    pivot = arr[high] #trying to put this number in its correct place
    i = low - 1 #set to i to -1, tracks elements that are smaller than pivot
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1 #if j is smaller/equal to pivot, we move i to the right
            arr[i], arr[j] = arr[j], arr[i] #we then swap the j element into i
    #loop ends hen all elements smaller than pivot are on the left of the array.
    #the original pivot is swapped into the position i+1. Pivot is where it needs to be.
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1 #returns index of pivot so quick_sort knows where the array was split

def quick_sort(arr, low, high):
    if low < high: #if not, the array is already sorted
        p = partition(arr, low, high) #gets pivot where everything to the left of p is smaller and to the right is bigger
        quick_sort(arr, low, p - 1) #recursion on the left array (<pivot)
        quick_sort(arr, p + 1, high) #recursion on the right array (>pivot)

    return arr

