num = int(input("Enter a number : "))

for i in range(1,num+1):
    for j in range(1,i+1):
        print(i,end = " ")
    print("")    


"""
output 

Enter a number : 4
1 
2 2
3 3 3
4 4 4 4
"""