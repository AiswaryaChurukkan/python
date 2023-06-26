'''list=[1,3,5,5,6,7,9]'''
'''print(list[10])'''
'''div=9
for i in list:
    i=div/0
print(i)'''

'''list=[1,2,3,4,5,6,7,8,9,10,11,66]
i=4
if i in list
    print("True")
else:
    print("False")'''


'''x=5
y=5
try:
    z=x+y
except TypeError:
    print("error")'''

n=int(input("Enter a number:"))
try:
 if n<0:
    print("fact is not found")
 elif n==0 or n==1:
    print("fact is 1")
 else:
    fact=1
    i=1

    while i<=n:
      fact=i*fact
      i+=1
  
    print("the fact value is:",fact)
except TypeError:
    print("error")