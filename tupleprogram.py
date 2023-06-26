#Python program to Find the size of a Tuple

'''import sys

Tuple1 = ("A", 1, "B", 2, "C", 3)
Tuple2 = ("Geek1", "Raju", "Geek2", "Nikhil", "Geek3", "Deepanshu")
Tuple3 = ((1, "Lion"), ( 2, "Tiger"), (3, "Fox"), (4, "Wolf"))

print("Size of Tuple1: " + str(sys.getsizeof(Tuple1)) + "bytes")
print("Size of Tuple2: " + str(sys.getsizeof(Tuple2)) + "bytes")
print("Size of Tuple3: " + str(sys.getsizeof(Tuple3)) + "bytes")'''


#Python – Maximum and Minimum K elements in Tuple

'''test_tup = (5, 20, 3, 7, 6, 8)

print("The original tuple is : " + str(test_tup))

K = 2

res = []
test_tup = list(sorted(test_tup))

for idx, val in enumerate(test_tup):
	if idx < K or idx >= len(test_tup) - K:
		res.append(val)
res = tuple(res)

print("The extracted values : " + str(res))'''


#Create a list of tuples from given list having number and its cube in each tuple

'''list1 = [1, 2, 5, 6, 7,9,6,8,2]

res = [(val, pow(val, 3)) for val in list1]

print(res)'''


#Python – Adding Tuple to List and vice – versa


'''list = [6, 7, 8, 9]

print("The original list is : " + str(list))

tup = (29, 67, 10)

list += tup

print("The container after addition : " + str(list))'''


#Python – Sum of tuple elements

'''def summation(test_tup):

	test = list(test_tup)

	count = 0

	for i in test:
		count += i
	return count

test_tup = (5, 20, 3, 7, 6, 8)
print(summation(test_tup))'''


#Python – Modulo of tuple elements

'''test_tup1 = (10, 4, 5, 6)
test_tup2 = (5, 6, 7, 5)

print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))

res = tuple(ele1 % ele2 for ele1, ele2 in zip(test_tup1, test_tup2))

print("The modulus tuple : " + str(res))'''


#Python – Row-wise element Addition in Tuple Matrix

'''test_list = [[('dfghy', 3), ('is', 3)], [('best', 1)], [('for', 5), ('geeks', 1)]]

print("The original list is : " + str(test_list))

cus_eles = [6, 7, 8]

res = [[sub + (cus_eles[idx], ) for sub in val] for idx, val in enumerate(test_list)]

print("The matrix after row elements addition : " + str(res))'''


#Python – Update each element in tuple list

'''test_list = [(1, 3, 4), (2, 4, 6), (3, 8, 1)]
print("The original list : " + str(test_list))
add_ele = 4
res = [tuple(j + add_ele for j in sub ) for sub in test_list]
print("List after bulk update : " + str(res))'''


#Python – Multiply Adjacent elements

'''test_tup = (1, 5, 7, 8, 10)

print("The original tuple : " + str(test_tup))

res = tuple(i * j for i, j in zip(test_tup, test_tup[1:]))

print("Resultant tuple after multiplication : " + str(res))'''


#Python – Join Tuples if similar initial element

'''test_list = [(5, 6), (5, 7), (6, 8), (6, 10), (7, 13)]

print("The original list is : " + str(test_list))

res = []
for sub in test_list:
	if res and res[-1][0] == sub[0]:
		res[-1].extend(sub[1:])
	else:
		res.append([ele for ele in sub])
res = list(map(tuple, res))

print("The extracted elements : " + str(res))'''


#Python – All pair combinations of 2 tuples

'''test_tuple1 = (4, 5)
test_tuple2 = (7, 8)

print("The original tuple 1 : " + str(test_tuple1))
print("The original tuple 2 : " + str(test_tuple2))

res = [(a, b) for a in test_tuple1 for b in test_tuple2]
res = res + [(a, b) for a in test_tuple2 for b in test_tuple1]

print("The filtered tuple : " + str(res))'''

#Python – Remove Tuples of Length K

'''test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]

print("The original list : " + str(test_list))

K = 1

res = [ele for ele in test_list if len(ele) != K]

print("Filtered list : " + str(res))'''


#Python – Remove Tuples from the List having every element as None

'''test_list = [(None, 2), (None, None), (3, 4), (12, 3), (None, )]

print("The original list is : " + str(test_list))

res = [sub for sub in test_list if not all(ele == None for ele in sub)]

print("Removed None Tuples : " + str(res))'''


#Sort a list of tuples by second Item

'''def Sort_Tuple(tup):

	lst = len(tup)
	for i in range(0, lst):

		for j in range(0, lst-i-1):
			if (tup[j][1] > tup[j + 1][1]):
				temp = tup[j]
				tup[j] = tup[j + 1]
				tup[j + 1] = temp
	return tup

tup = [('for', 24), ('is', 10), ('Geeks', 28),
	('Geeksforgeeks', 5), ('portal', 20), ('a', 15)]

print(Sort_Tuple(tup))'''


#Python – Sort Tuples by Total digits

'''def count_digs(tup):
	
	return sum([len(str(ele)) for ele in tup ])

test_list = [(3, 4, 6, 723), (1, 2), (12345,), (134, 234, 34)]

print("The original list is : " + str(test_list))

test_list.sort(key = count_digs)

print("Sorted tuples : " + str(test_list))'''


#Python – Elements frequency in Tuple

'''from collections import defaultdict

test_tup = (4, 5, 4, 5, 6, 6, 5, 5, 4)

print("The original tuple is : " + str(test_tup))

res = defaultdict(int)
for ele in test_tup:
	
	res[ele] += 1

print("Tuple elements frequency is : " + str(dict(res)))'''

#Python – Filter Range Length Tuples

'''test_list = [(4, ), (5, 6), (2, 3, 5), (5, 6, 8, 2), (5, 9)]

print("The original list is : " + str(test_list))

i, j = 2, 3

res = [sub for sub in test_list if len(sub) >= i and len(sub) <= j]
print("The tuple list after filtering range records : " + str(res))'''


#Python – Assign Frequency to Tuples

'''from collections import Counter

test_list = [(6, 5, 8), (2, 7), (6, 5, 8), (6, 5, 8), (9, ), (2, 7)]

print("The original list is : " + str(test_list))

res = [(*key, val) for key, val in Counter(test_list).items()]

print("Frequency Tuple list : " + str(res))'''


#Python – Records with Value at K index

'''test_list = [(3, 1, 5), (1, 3, 6), (2, 5, 7), (5, 2, 8), (6, 3, 0)]

print("The original list is : " + str(test_list))

ele = 3

K = 1

res = []
for x, y, z in test_list:
	if y == ele:
		res.append((x, y, z))

print("The tuples of element at Kth position : " + str(res))'''

#Python – Test if tuple is distinct

test_tup = (1, 4, 5, 6, 1, 4)

print("The original tuple is : " + str(test_tup))

res = True
temp = set()
for ele in test_tup:
	if ele in temp:
		res = False
		break
	temp.add(ele)

print("Is tuple distinct ? : " + str(res))
