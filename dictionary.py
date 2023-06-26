'''mydict={1:'apple',2:34,3:[4,7,9]}
print(mydict)'''

'''mydict=dict ({1:45,2:56,3:78})
print(mydict)
print(type(mydict))
#print (mydict[5])
#print(mydict.get(5))'''

#add and update
'''mydict[2]=65
print(mydict)
mydict[4]=90
print(mydict)

#pop
print(mydict.pop(1))
print(mydict)
print(mydict.popitem())
print(mydict)

#clear
print(mydict.clear())
print(mydict)

#delete
del mydict
print(mydict)'''

'''#fromkeys
marks={}.fromkeys(['mat','eng','sci'],78)
print(marks)

#items
for x in marks.items():
    print(x)

 #sort
print(list(sorted(marks.keys())))

#convert the list two dictionary
li1=[1,2,3,4,5,6,7]
li2=['apple','orange','kiwi','banana','mango']
result=dict(zip(li1,li2))
print(result)'''

#electricity
units=int(input("Enter the number of unit :"))
if( units <= 100 ):
  amount=units * 0.5
  print(amount)

elif (units>=101 and units <= 150):
  amount=units * 0.75
  print(amount)

elif (units>=150 and units <=200):
  amount=units * 1
  print(amount)

elif (units >=200 ):
  amount=units * 2
  print(amount)
