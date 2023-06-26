#Find the size of a Set in Python
'''import sys
Set1 = {"A", 1, "B", 2, "C", 3}
Set2 = {"Geek1", "Raju", "Geek2", "Nikhil", "Geek3", "Deepanshu"}
Set3 = {(1, "Lion"), ( 2, "Tiger"), (3, "Fox")}
print("Size of Set1: " + str(sys.getsizeof(Set1)) + "bytes")
print("Size of Set2: " + str(sys.getsizeof(Set2)) + "bytes")
print("Size of Set3: " + str(sys.getsizeof(Set3)) + "bytes")'''


#Iterate over a set in Python

'''set = set("pythonprogram")
for val in set:
    print(val)'''

#Python – Maximum and Minimum in a Set


'''     
set = set([8, 16, 24, 1, 25, 3, 10, 65, 55])
print(max(set))
print(min(set))'''

#Python – Remove items from Set

'''set = {12, 10, 13, 15, 8, 9}
set.remove(10)
print(set)'''

#Python – Check if two lists have at-least one element common

list1= [1, 2, 3, 4, 5]
list2= [5, 6, 7, 8, 9]
print(list1, list2):

for x in a:
 
        for y in list2:
   
            if x == y:
                result = True
                return result            
    return result
a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
print(common_data(a, b))
 
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9]
print(common_data(a, b))


#Python program to find common elements in three lists using sets
'''def find_common(list1, list2, list3):
    common = set()
    for elem in list1:
        if elem in list2 and elem in list3:
            common.add(elem)
    return common
 
list1 = [1, 5, 10, 110, 40, 90]
list2 = [6, 7, 110, 90, 100]
list3 = [3, 4, 15, 110, 30, 70, 90, 120]
 
common = find_common(list1, list2, list3)
print(common)'''

#Python – Find missing and additional values in two lists

'''list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8]
print("Missing values in second list:", (set(list1).difference(list2)))
print("Additional values in second list:", (set(list2).difference(list1)))
print("Missing values in first list:", (set(list2).difference(list1)))
print("Additional values in first list:", (set(list1).difference(list2)))'''

#Python program to find the difference between two lists

'''list1 = [10, 15, 20, 25, 30, 35, 40,55]
list2 = [25, 40, 35]
 
temp3 = []
for element in list1:
    if element not in list2 :
        temp3.append(element)
 
print(temp3)'''

#Python Set difference to find lost element from a duplicated array
 
'''def lostElement(A,B):

    A = set(A)
    B = set(B)
 
    if len(A) > len(B):
        print (list(A-B))
    else:
        print (list(B-A))

if __name__ == "__main__":
    A = [1, 4, 5, 7, 9]
    B = [4, 5, 7, 9]
    lostElement(A,B)'''

#Python program to count number of vowels using sets in given string

'''def vowel_count(str):
    count = 0
    vowel = set("sdfhfgRDFGHJ")
    for alphabet in str:
        if alphabet in vowel:
            count = count + 1
     
    print("No. of vowels :", count)

str = "GeeksforGeeks"

vowel_count(str)'''

#Concatenated string with uncommon characters in Python

'''def uncommonConcat(str1, str2):
    set1 = set(str1)
    set2 = set(str2)
    common = list(set1 & set2)
    result = [ch for ch in str1 if ch not in common] + [ch for ch in str2 if ch not in common]
    print( ''.join(result) )
if __name__ == "__main__":
    str1 = 'dfghyy'
    str2 = 'retyuyiukhgh'
    uncommonConcat(str1,str2)'''

#Python – Program to accept the strings which contains all vowels

'''def check(string) :

	string = string.lower()

	vowels = set("aeiou")

	s = set({})

	for char in string :

		if char in vowels :
			s.add(char)
		else:
			pass

	if len(s) == len(vowels) :
		print("Accepted")
	else :
		print("Not Accepted")

if __name__ == "__main__" :
	
	string = "gfdtfyguhrdy"
	check(string)'''


#Python – Check if a given string is binary string or not

'''def check(string):
	p = set(string)

	s = {'0', '1'}

	if s == p or p == {'0'} or p == {'1'}:
		print("Yes")
	else:
		print("No")

if __name__ == "__main__":

	string = "101010000111"

	check(string)'''


#Python set to check if string is pangram

'''from string import ascii_lowercase as asc_lower

def check(s):
	return set(asc_lower) - set(s.lower()) == set([])

string ="The quick brown fox jumps over the lazy dog"
if(check(string)== True):
	print("The string is a pangram")
else:
	print("The string isn't a pangram")'''


#Python Set – Pairs of complete strings in two sets

'''def completePair(set1,set2):

	count = 0
	for str1 in set1:
		for str2 in set2:
			result = str1 + str2

			tmpSet = set([ch for ch in result if (ord(ch)>=ord('a') and ord(ch)<=ord('z'))])
			if len(tmpSet)==26:
				count = count + 1
	print (count)

if __name__ == "__main__":
	set1 = ['abcdefgh', 'geeksforgeeks','lmnopqrst', 'abc']
	set2 = ['ijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz','defghijklmnopqrstuvwxyz']
	completePair(set1,set2)'''

#Python program to check whether a given string is Heterogram or not

'''def is_heterogram(string):
	sorted_string = sorted(string.lower())
	for i in range(1, len(sorted_string)):
		if sorted_string[i] == sorted_string[i-1] and sorted_string[i].isalpha():
			return 'No'
	return 'Yes'
string='the big dwarf only jumps'
print(is_heterogram(string))'''

#Python program to convert Set into Tuple and Tuple into Set

'''s = {'a', 'b', 'c', 'd', 'e'}

print(type(s), " ", s)

t = tuple(s)

print(type(t), " ", t)'''


#Python program to convert set into a list

'''my_set = {'Geeks', 'for', 'geeks'}
 
s = list(my_set)
print(s)'''

#Python program to convert Set to String

'''s = {'a', 'b', 'c', 'd'}
print("Initially")
print("The datatype of s : " + str(type(s)))
print("Contents of s : ", s)

s = str(s)
print("\nAfter the conversion")
print("The datatype of s : " + str(type(s)))
print("Contents of s : " + s)'''

#Python program to convert String to Set

'''string = "geeks"
print("Initially")
print("The datatype of string : " + str(type(string)))
print("Contents of string : " + string)

string = set(string)
print("\nAfter the conversion")
print("The datatype of string : " + str(type(string)))
print("Contents of string : ", string)'''


#Python – Convert a set into dictionary

'''ini_set = {1, 2, 3, 4, 5}

print ("initial string", ini_set)
print (type(ini_set))

res = dict.fromkeys(ini_set, 0)

print ("final list", res)
print (type(res))'''
