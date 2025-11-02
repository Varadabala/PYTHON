#1.	Consecutive Triplet Sum: Write a function that takes a list of integers and an integer k. 
# Return True if there are three consecutive elements in the list whose sum is exactly k, otherwise return False.

def consecutive_triplet_sum(nums, k):
    for i in range(len(nums) - 2):  
        triplet_sum = nums[i] + nums[i+1] + nums[i+2]
        if triplet_sum == k:
            return True
    return False
nums = [2, 4, 1, 3, 5]
print(consecutive_triplet_sum(nums, 8))
print(consecutive_triplet_sum(nums, 10))

'''
output
True
False
'''