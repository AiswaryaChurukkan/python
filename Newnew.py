#python program to find sum and average of list in python

'''mylist=[4 , 7, 8 , 5 , 8 , 7 , 2 , 3 , 4]
count=0
for i in mylist:
    count+=i
avg=count/len(mylist)
print("sum of mylist:",count)
print("average of a mylist:",avg)'''


#python program to find second largest number in a list
'''mylist=[4 , 7, 8 , 5 , 8 , 7 , 2 , 3 , 4]
mylist.sort()
print("second largest number :",mylist[-2])'''

#python program to find smallest number in a list
'''mylist=[4 , 7, 8 , 5 , 8 , 7 , 2 , 3 , 4]
mylist.sort()
print("smallest number :",mylist[0])'''

#python program to find the size of a tuple
'''tuple=(4 , 7, 8 , 5 , 8 , 7 , 2 , 3 , 4)
print(tuple.sizeof())
print(dir(tuple))'''

#sort a list of tubles by second item
'''mylist=(4 , 7, 8 , 5 , 8 , 7 , 2 , 3 , 4)
mylist.sort()
print("second item:",mylist[1])'''

#python program to capitalize the first and last character of each word in a string
'''word="Happy New Year"
print(word.capitalize())'''


#python count the number of matching characters in a pair of string

'''mylist=(4 , 7, 8 , 5 , 8 , 7 , 2 , 3 , 4)
print(mylist.count(8))'''

#python program for removing i-th character from a string
str="welcome to python"
str2=""
for i in range(len(str)):
     if i !=2:
        str2=str2+str[i]
print("the string after removel of i th character:"+str2)
li=[2,6,4,7,8,9]
print(li)
size=len(li)
temp=li[0]
li[0]=li[size-1]
li(size-1==temp)
print("after swapping list")
print(list)

