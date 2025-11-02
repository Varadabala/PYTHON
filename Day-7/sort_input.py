#4.	Take input from user (list or tuple). 
# Write a function which can sort the given input in either ascending(default) or descending(if a parameter reverse = True is passed while calling the function).
#  Return a sorted list if the user inputs a list else return a tuple.

def sort_list():
    # Ask user for numbers
    user_input = input("Enter numbers separated by spaces: ")

    # Convert string input into list of integers
    data = [int(x) for x in user_input.split()]

    # Sort in ascending and descending order
    ascending = sorted(data) # [1,2,3,4,5]
    descending = sorted(data, reverse=True) #[5,4,3,2,1]

    # Print results
    print("Ascending order:", ascending)
    print("Descending order:", descending)


sort_list()

'''
Enter numbers separated by spaces: 1 2 3 6 8 4 
Ascending order: [1, 2, 3, 4, 6, 8]
Descending order: [8, 6, 4, 3, 2, 1]
'''