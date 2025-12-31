#continue -- > it skips the current iteration when it mets the condition and works asusual

#Program: Skip even numbers
n = int(input("Enter a number : "))
for i in range(1, n):
    if i % 2 == 0:
        continue
    print(i,end = " ")
