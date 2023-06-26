bus={
    "Routeno":5,
    "Driver ":"Kiran",
    "cleaner": "Manu",
    "Points":["karamana","PMG","pattom"]
}

print(bus["Driver"])
print(bus.get("Driver"))
print (bus.keys())
print (bus.values())
print (bus.items())
bus["color"]="Red"

bus ["Driver"]="Mohan"
print(bus)
'''bus.pop("fare")'''
bus.popitem()
print(bus)
'''del bus["Fare"]
del bus
bus.clear()'''


for x in bus:
    print(x)
for x in bus :
    print(bus[x])

bus.clear()
print(bus)

# print(student) => {name: kiran, age: 25....}

'''student={"name":"Kiran",
          "age":25, 
          "mark1":76, 
          "mark2":85}
student["name"] 
print(student)
student.get("name") 
print(student)
student.keys() 
print(student)
student.values() 

student["name"]="Manu" 
print(student)
student["phone"]=958744123 
print(student)
student.update({"name":"Mohan"}) 
print(student)
student.update({"Address":"Kottayam"}) '''


# student.pop("name") 
# student.popitem() 
# del student["name"] 
# del student 
# student.clear() 
# candidate=student.copy()
# candidate=dict(student) 
# print(student)
# print(dict)

# # print(student) => {name: kiran, age: 25....}



'''contactlist={}
n=int (input("Enter the number of contacts :"))
for i in range(1,n+1):
    name=input("Enter the contact name:")
    phno=int(input("Enter the phone number:"))
    contactlist[name]=phno
print("keys")
for x in contactlist.keys():
    print(x)
print("values")
for x in contactlist.values():
    print(x)
print("keys-value pairs")
for x,y in contactlist.items():
    print(x,"-",y)'''


'''numberNames={0:'Zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
positionvalues={0:'ones',1:'Tens',2:'Humdreds',3:'Thousands',5:'Lakhs',6:'Ten Lakhs',7:'Crore',8:'Ten Crore'}
num=input("Enter any number :")
result=''
l=len(num)-1
for ch in num:
    key=int (ch)
    value=numberNames[key]
    result=result + ' ' + value+ ' '+ positionvalues[1]
    l-=1
print("The number is :",num)
print("The number Name is :",result)'''