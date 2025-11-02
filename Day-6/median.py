#2.	Rotate List and Find Median (Left or Right):
#  Write a Python function that takes a list of numbers, a rotation count k,
#  and a direction ('left' or 'right'). 
# First, sort the list manually using bubble sort (do not use any built-in sorting methods).
# Then, rotate the sorted list by k positions,
#  If direction is 'left', perform a left rotation, If direction is 'right', perform a right rotation.
#  Finally, find and return the median of the rotated list without using any predefined median functions.

def rotate_and_median(lst, k, direction):
  
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    
    k = k % n  
    if direction == 'left':
        rotated = lst[k:] + lst[:k]
    elif direction == 'right':
        rotated = lst[-k:] + lst[:-k]
    else:
        return "Invalid direction"

    
    n = len(rotated)
    if n % 2 == 1:
        median = rotated[n // 2]
    else:
        median = (rotated[n // 2 - 1] + rotated[n // 2]) / 2

    return rotated, median

lst = [5, 2, 8, 1, 3]
print(rotate_and_median(lst, 2, 'right'))
