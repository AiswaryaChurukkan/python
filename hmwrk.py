# Python3 program to swap firstand last element of a list
'''def swapList(newList):
     
    newList[0], newList[-1] = newList[-1], newList[0]
 
    return newList
     
newList = [12, 35, 9, 56, 24]
print(swapList(newList))'''
# Python3 program to swap elements at given positions
'''def swapPositions(list, a, b):
     
    list[a], list[b] = list[b], list[a]
    return list
 
List = [23, 65, 19, 90]
a, b  = 1, 4
print(swapPositions(List, a-1, b-1))'''
#Python  Ways to find length of list
list=[4,7,9,5,6]
print(len(list))
#Maximum of two numbers in Python
list=[6,9,3,5]
print(max(list))
#Minimum of two numbers in Pythonli
st=[6,9,3,5]
print(min(list))
#Python  Ways to check if element exists in list
li=[3,4,6,2,8,9]
i=9
if i in li:
    print("exist")
else:
    print("not exist")

#Different ways to clear a list in Python
list=[3,4,6,2,8,9]
list.clear()
print(list)

#Python Reversing a List
list=[3,4,6,2,8,9]
list.reverse()
print(list)
#Python Cloning or Copying a list


#Python Count occurrences of an element in a list
#Python Program to find sum and average of List in Python
list=[45,87,2,3,4]
count=0
for i in list:
    count+=i
avg=count/len(list)
print("sum of list:",count)
print("average of a list:",avg)
#Python | Sum of number digits in List
list=[1,4,5,7,8]


#Python Multiply all numbers in the list
#Python program to find smallest number in a list
list=[87,2,5,6,71,92]
list.sort()
print("smallest number is:",list[0])
#ython program to find largest number in a list
list=[87,2,5,6,71,92]
list.sort()
print("second largest number is:",list[-1])
#Python program to find second largest number in a list
list=[87,2,5,6,71,92]
list.sort()
print("second largest number is:",list[-2])
#Python program to print even numbers in a list
list=[34,56,78,45,3]
for i in list: 
 if i%2==0:
    print("even numbers",i)
#Python program to print all odd numbers in a range
list=[34,56,78,45,3]
for i in list: 
 if i%2!=0:
    print("odd numbers",i)
#Python program to count Even and Odd numbers in a List
a = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15) 
even , odd = 0,0
for num in a:
    if num % 2 == 0 :
        even+=1
    else:
        odd+=1
print("odd number:",odd)
print("even number:",even)
#Python program to print positive numbers in a list
list=[-1,5,3,8,-6,9]
for i in list:
   if i>=0:
      print("positive numbers:",i)
#Python program to print negative numbers in a list
list=[-1,5,3,8,-6,9]
for i in list:
   if i<=0:
      print("negative  numbers:",i)
#Python program to print all positive numbers in a range
for i in range(-2,10):
   if i>=0:
        print("positive numbers:",i)
#Python program to print all negative numbers in a range
for i in range(-9,10):
   if i<=0:
        print("negative numbers:",i)
#Python program to count positive and negative numbers in a list
list=[-1,4,5,-3,6,-7]
positive=0
negative=0
for i in list:
   if i>=0:
      positive+=1
   else:
      negative+=1
print("positive numbers:",positive)
print("negative numbers",negative)
#Remove multiple elements from a list in Python
list=[34,5,6,7,8,7,5]
list.remove[5]
#Python Remove empty tuples from a list
#Python Program to print duplicates from a list of integers
