min=int(input("Enter the minimum:"))
max=int(input("Enter the maximum"))
print("numbers which are divisible by 7 and multiple of 5:")
i=min
while(i<=max):
    if(i%7==0 and i%5==0):
        print(i)
    i+=1