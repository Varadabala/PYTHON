#3. Lambda for Recursive Fibonacci: Using a single line of code with a lambda function 
# and appropriate helper methods (no explicit def or while/for loop), 
# generate the first 5 terms of the Fibonacci sequence.

#method-1
fib = lambda n: n if n <= 1 else fib(n-1) + fib(n-2)
print([fib(i) for i in range(5)])


#method-2
fib = lambda n, a=0, b=1: [] if n == 0 else [a] + fib(n-1, b, a+b)
print(fib(5))

