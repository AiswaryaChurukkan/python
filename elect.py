
'''bill=int(input("enter the unit of charge :"))
if bill<=100: 
    d=bill*0.50 
    print(d) 
elif bill>100 and bill<=150: 
    d=((bill-100)*0.75)+(100*0.50)
    print(d) 
elif bill>150 and bill<=200: 
    d=((bill-150)*1)+(50*0.75)+(100*0.50) 
    print(d)
elif bill>200: 
    d=(50*0.75)+(100*0.50)+(50*1)+((bill-200)*2)
    print(d) 
else: 
    pass'''


'''type=input("Enter the type of connection :") 
u=int(input("Enter the units consumed : "))
charge=0 
if type=="domestic": 
    if u<=100: 
        charge=u*1 
    elif u<150: 
        charge (100*1)+(u-100)*1.5 
    elif u<=200: 
        charge (100*1)+(50*1.5)+(u-150)*2 
    else: 
        charge=(100*1)+(50*1.5)+(50*2)+(u-200)*3
elif type=="commercial":
    if u<=100: 
        charge=u*3 
    elif u<150: 
        charge (100*3)+(u-100)*4 
    elif u<=200: 
         charge=(100*3)+(50*4)+(u-150)*6 
    else:
         charge (100*3)+(50*4)+(50*6)+(u-200)*10 
else: 
    print("Invalid connection type ") 
    print("Tarriff: ",charge)'''
#automorphic and trimorphic

num=int(input("Enter the number : ")) 
print("Menu") 
print("1.Automorphic")
print("2. Trimorphic")
choice=int(input("Enter your choice : "))
l=len(str(num))
if choice==1:
    sq=num*2 
    if sq%(101)==num: 
         print(num," is automorphic") 
    else: 
         print(num," is not automorphic") 
elif choice==2:
       cb=num
       if cb% (10*1)==num: 
         print(num," is trimorphic") 
       else: 
         print(num," is not trimorphic")
else:
    
     print("Invalid choice!!!")


#listduplicate.py 
'''a=[]
n= int(input("Enter the number of elements : ")) 
print("Enter the elements : ") 
for i in range(0,n): 
    k=int(input())
    a.append(k) 
i=0 
while i<n-1: 
    j=i+1 
    while j<n: 
        if a[i]==a[j]: 
            a.pop(j) 
            n=n-1 
        else: 
            j+=1 
    i+=1 
print(a)'''

#listbig.py
'''a=[] 
n= int(input("Enter the number of elements : ")) 
print("Enter the elements: ") 
for i in range(0,n): 
    k=int(input()) 
    a.append(k) 
big=a[0] 
for i in range(1,n): 
    if a[i]>big: 
        big=a[i] 
print("Biggest : ",big)'''

#listcount.py 
'''a=[] 
n= int(input("Enter the number of elements : ")) 
print("Enter the elements : ") 
for i in range(0,n): 
    k=int(input()) 
    a.append(k)
count=0
ele=int(input("Enter the element to count : ")) 
for x in a: 
    if x==ele: 
         count+=1 
print(ele," occured ",count," times")'''

#listdelete.py 
'''a=[] 
n= int(input("Enter the number of elements : ")) 
print("Enter the elements : ") 
for i in range(0,n): 
    k=int(input()) 
    a.append(k) 
index=int(input("Enter the index : "))
for i in range(index,n-1): 
    a[i]=a[i+1] 
n=n-1 
print("List elements are: ") 
for i in range(0,n): 
    print(a[i])'''