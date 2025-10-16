#4. Create a function that returns multiple values (min, max, sum) of a list.
# (Write only user defined functions and make use of those to calculate max, min and sum)

def min_num(numbers):
    min = numbers[0]
    for i in numbers:
        if i< min:
            min = i
    return min

def max_num(numbers):
    max = numbers[0]
    for i in numbers:
        if i > max:
            max = i
    return max

def find_sum(numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum 

def combine_func(numbers):
    return find_sum,max_num,min_num     

numbers = [1,2,3,4,5]
find_sum,max_num,min_num = combine_func(numbers)
#numbers = list(map(int,input().split()))
print("Sum = ",find_sum(numbers))
print("Max Value = ",max_num(numbers))

print("Min Value = ",min_num(numbers))



"""
output 

Sum =  15
Max Value =  5
Min Value =  1


"""
