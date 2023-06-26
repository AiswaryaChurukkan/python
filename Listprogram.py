#Python program to interchange first and last elements in a list
'''list=[1,2,3,4,5,6,7,8,9]
print("before swapping:",list)
list[0] ,list[-1] =list[-1] ,list[0]
print("after swapping:",list)'''

#Python program to swap two elements in a list
'''list=[1,2,3,4,5,6,7,8,9]
print("before swapping:",list)
list[2] ,list[-1] =list[-1] ,list[2]
print("after swapping:",list)'''


#or

'''def mylist(list, pos1, pos2):
     
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list
List = [1,2,3,4,5,6,7,8,9]
pos1, pos2  = 1, 9
 
print(mylist(List, pos1-1, pos2-1))'''


#Python – Swap elements in String list
'''list=['apple','orange','cherry','banana','kiwi']
print("orginal list:",list)
res = [sub.replace('a', '-').replace('e', 'a').replace('-', 'e') for sub in list]
print("List after performing character swaps :", list)'''

#Python | Ways to find length of list
'''list=[1,2,3,4,5,6,7,8,9]
print(len(list))'''

#Maximum of two numbers in Python
'''list=[1,2,3,4,5,6,7,8,9,10,11,66]
print(max(list))

#Minimum of two numbers in Python
print(min(list))'''

#Python | Ways to check if element exists in list

'''list=[1,2,3,4,5,6,7,8,9,10,11,66]
i=4
if i in list:
    print("True")
else:
    print("False")'''


#Different ways to clear a list in Python

'''list=[1,2,3,4,5,6,7,8,9,10,11,66]
print("list after clear:",list)
list.clear()
print("list before clear:",list)'''

#Python | Reversing a List

'''list=[1,2,3,4,5,6,7,8,9,10,11,66]
print("list after reversing:",list)
list.reverse()
print("list before reversing:",list)'''

#Python | Cloning or Copying a list

'''list=[1,2,3,4,5,6,7,8,9,10,11,66]
print("list after coppy:",list)
list.copy()
print("list before coppy:",list)'''

#Python | Count occurrences of an element in a list

'''list=[1,2,3,4,7,7,7,5,6,7,8,9,10,11,66]
print(list.count(7))'''

#Python Program to find sum and average of List in Python

'''list=[1,2,3,4,7,7,7,5,6,7,8,9,10,11,66]
print(list)
sum=0
i=0
while i<len(list):
    sum+=list[i]
    i+=1
print("sum of list=",sum)
avg=sum/len(list)
print("average of list=",avg)'''

#Python | Sum of number digits in List

'''list=[1,2,3,4,5]
print(list)
sum=0
i=0
while i<len(list):
    sum+=list[i]
    i+=1
print("sum of numbers digits in  list=",sum)'''

#Python | Multiply all numbers in the list

'''def multiplyList(myList):
    result = 1
    for x in myList:
        result = result * x
    return result
 
list1 = [1,2,3,4,7,7,7,5,6,7,8,9,10,11,66]
list2 = [1,2,3,4,7,7,7,5,6,7,8,9,10,11,66]
print(multiplyList(list1))
print(multiplyList(list2))'''

#Python program to find smallest number in a list

'''list = [1,2,3,4,7,7,7,5,6,7,8,9,10,11,66]
list.sort()
print ("smallest number in a list :",list[0])'''

#Python program to find largest number in a list

'''list = [1,2,3,1000,4,7,7,7,5,90,6,7,8,9,10,11,66]
list.sort()
print ("largest number in a list :",list[-1])'''

#Python program to find second largest number in a list

'''list = [1,2,3,1000,4,7,7,7,101,5,90,6,7,8,9,10,11,66]
list.sort()
print ("Second largest number in a list :",list[-2])'''

#Python program to print even numbers in a list
'''list = [1,2,3,1000,4,7,7,7,101,5,90,6,7,8,9,10,11,66]
for num in list:
    if num % 2 == 0:
        print(num, end=" ")   '''


#Python program to print odd numbers in a List
'''list1 = [1,2,3,1000,4,7,7,7,101,5,90,6,7,8,9,10,11,66]
for num in list1:
    if num % 2 != 0:
       print(num, end=" ")'''


 
#Python program to print all even numbers in a range

'''for even_numbers in range(4,15,2):
    print(even_numbers,end=' ')'''


#Python program to print all odd numbers in a range

'''start, end = 9,50
for num in range(start, end + 1):
     
    if num % 2 != 0:
        print(num, end = " ")'''

#Python program to count Even and Odd numbers in a List

'''a = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15) 
even , odd = 0,0
for num in a:
    if num % 2 == 0 :
        even+=1
    else:
        odd+=1
print("odd number:",odd)
print("even number:",even)'''

#Python program to print positive numbers in a list

'''list = [-10, 21, -4, -45,55,-87,95,70, -66, 93]
num = 0   
while(num < len(list)):
    if list[num] >= 0:
        print(list[num], end = " ")
    num += 1'''


#Python program to print negative numbers in a list

'''list = [-10, 21, -4, -45,55,-87,95,70, -66, 93]
for num in list:
    if num < 0:
     print(num, end=" ")'''


#Python program to print all positive numbers in a range

'''start, end = -4, 19
for num in range(start, end + 1):
    if num >= 0:
        print(num, end=" ")'''

#Python program to print all negative numbers in a range

'''def negativenumbers(a,b):
  out=[i for i in range(a,b+1) if i<0]
  print(*out)
a=-4
b=5
negativenumbers(a,b)'''

#Python program to count positive and negative numbers in a list

'''list1 = [10, -21, 4, -45, 66, -93, 1]
 
postivecount, negativecount = 0, 0
 
for num in list1:

    if num >= 0:
       postivecount += 1
 
    else:
       negativecount += 1
 
print("Positive numbers in the list: ",postivecount)
print("Negative numbers in the list: ", negativecount)'''

#Remove multiple elements from a list in Python

'''list = [11, 5, 17, 18, 23, 50, 87, 35, 45, 44]
for element in list:
    if  element % 2 == 0:
        list.remove( element)
print("New list after removing all even numbers: ", list)'''

#Python | Remove empty tuples from a list

tuples = [(), ('adhi','26','3'), (), ('rama', 'athira'),
          ('krishna', 'haritha', '35'), ('',''),()]
t = tuples
tuples.remove(t)
print(tuples)



#Python | Program to print duplicates from a list of integers

'''lis = [1,2,3,1000,4,7,7,7,101,5,90,9,5,6,3,1,1,2,2,89,8,9,6,7,8,9,10,11,66]
 
uniqueList = []
duplicateList = []
 
for i in lis:
    if i not in uniqueList:
        uniqueList.append(i)
    elif i not in duplicateList:
        duplicateList.append(i)
 
print(duplicateList)
'''