li=[1,2,3,4,5,6]


def addnumber(li):
    li.append(7)
    print(li)

addnumber(li)


def avgnumber(li):
    avg=str(li)
    count=0
    for i in li:
     count+=i
    avg=count/len(li)
    print(avg)

avgnumber(li)