a = [10,89,9,56,4,80,8]
min = a[0]
max = a[0]
for i in range(0, len(a)):
    if(min < a[i]):
        min = a[i]
    elif(max > a[i]):
        max = a[i]
print("Smallest number= ",min)
print("Largest number= ",max)
