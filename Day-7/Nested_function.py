#2.Curried Multiplier Closure: Write a function create_multiplier(x) that
#returns a nested function multiplier(y). The inner function should calculate
#and return x times y. Use the nonlocal keyword to allow a third nested
#function, reset_x(), to change the value of x in the create_multiplier scope.
def something(x):
   def another(y):
       return x*y
   def about(arg):
       nonlocal x
       x=arg
   return another,about        
multiply, reset = something(5)
print("Initial multiply(3):", multiply(3))   
reset(10)                                    
print("After reset multiply(3):", multiply(3))  


'''
output
Initial multiply(3): 15
After reset multiply(3): 30
'''