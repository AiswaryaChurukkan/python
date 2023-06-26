#3
'''list=[87,2,5,6,71,92]
list.sort()
print("smallest number is:",list[0])'''
#'''1
'''list=[45,87,2,3,4]
count=0
for i in list:
    count+=i
avg=count/len(list)
print("sum of list:",count)
print("average of a list:",avg)
#2
list=[87,2,5,6,71,92]
list.sort()
print("second largest number is:",list[-2])'''
#4
'''tuple=(2,5,6,8,9)
print(tuple.sizeof())'''
#5
'''t=(4,5,6,7,34,56)
t.sort([1])
#6
str="welcome to python"
print(str.capitalize())'''
#8
'''str="welcome to python"
str2=""
for i in range(len(str)):
     if i !=2:
        str2=str2+str[i]
print("the string after removel of i th character:"+str2)'''
li=[2,6,4,7,8,9]
print(li)
size=len(li)
temp=li[0]
li[0]=li[size-1]
li(size-1==temp)
print("after swapping list")
print(list)
