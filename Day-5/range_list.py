#3. Use range to print the index and value of a list simultaneously.

list1 = input("Enter a lsit values : ").split()
print(list1)
dict = {}
for  i in range(0,len(list1)):
    print(f"index : {i} , value : {list1[i]}")
    #dict[i]=list1[i]
#print(dict)

"""
output 

Enter a list values : Bala Varada Dhoni
['Bala', 'Varada', 'Dhoni']
index : 0 , value : Bala
index : 1 , value : Varada
index : 2 , value : Dhoni

"""
