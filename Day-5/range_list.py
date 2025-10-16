#3. Use range to print the index and value of a list simultaneously.

list1 = input("Enter a lsit values : ").split()
print(list1)
dict = {}
for  i in range(0,len(list1)):
    print(f"index : {i} , value : {list1[i]}")
    #dict[i]=list1[i]
#print(dict)
