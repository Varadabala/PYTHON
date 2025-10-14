# Create a list from user input, find duplicates, and return a set of those duplicates.

user =list(map(int,input("Enter a list of elements : ").split()))
a={}

for i in user:
    if i in  a:
        a[i]+=1
    else:
        a[i]=1
print(a)
b=list()
for j,k in a.items():
    if k>1:
        b.append(j)
print(set(b))

"""
output 

Enter a list of elements : 1 2 3 1 3 2
{1: 2, 2: 2, 3: 2}
{1, 2, 3}
"""



"""
def even_odd(n):
    if n%2==0:
        return n
    else:
        return "odd"
a=[1,2,3,4,5,6,7,8]
b=list(map(even_odd,a))
print(b)
"""