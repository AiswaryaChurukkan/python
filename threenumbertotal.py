a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
c=int(input("Enter the number:"))
Total = a+b+c
print("Total of three num:",Total) 
avg = Total/3
print(avg)
if(avg<=100 and avg<=90):
    print("A")
elif(avg<80 and avg<=70):
    print("B")
elif(avg<60 and avg<=50):
    print("C")
elif(avg<40 and avg<=30):
    print("D")
elif(avg<20 and avg<=10): 
       print("E") 
else:
    print("F")