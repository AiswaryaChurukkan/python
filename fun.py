
'''def sum():
    a=19
    b=45
    c=a+b
    print(c)
sum()'''

'''def fact(n):
 n=int(input("Enter a number:"))
 if n<0:
    print("fact is not found")
 elif n==0 or n==1:
    print("fact is 1")
 else:
    fact=1
    i=1
    while i<=n:
      fact=i*fact
      i+=1
    print("the fact value is:",fact)
fact(30)'''


'''def sum(a,b):
   c=a+b
   print(c)
sum(14,98)'''

'''def sum(a=10,b=20):
  c=a+b
  print(c)
sum()'''

'''def sub(a=10,b=20):
  c=a-b
  print(c)
sub()
sub()

def mul(*x):
  print(x)
mul(89,43,34)

def mul(a=14,b=43,c=34):
  d=a*b*c
  print(d)
mul()'''

#vowels
'''list1=['p','y','t','h','o','n']

def countvowl(string):
  vowel="aeiouAEIOU"
  count=0
  for i in list1:
    if(i in vowel):
      count+=1
      print(i)
  print(count)

  
countvowl(list1)'''
  

#or
'''
def count():
  list=['p','y','t','h','o','n']
  voels=['a','e','i','o','u','A','E','I','O','U']
  count=0
  for i in list:
    if '''

'''num = 1234
def sum(num):
    str1 = str(num)
    s = 0
    for i in str1:
        a = int(i)
        s = s + a
    print(s)

sum(num)'''


# palindrom

'''num = 121
def reverse(num):
    str1 = str(num)
    rev = str1[::-1]
    if(rev == str1):
        print("palin")
    else:
        print("not")
reverse(num)'''


'''num=657
def sub(num):
    str1=str(num)
    s=0
    for i in str1:
        a=int(i)
        s=a-s
        print(s)
sub(num)'''

#orbitary

'''def number(*num):
  s=0
  for i in num:
      s=s+i
  print(s)
number(3,2)'''

#or

'''def flat(*x):
    s=0
    for i in x:
        s=s+i
    print(s)
flat(1,2,3,4,5,6,7,8,9)'''
        
#keyword

'''def number(a=10,b=80):
    s=0
    for i in a,b:
        s=s+i
    print(s)
number()
         '''

#reference


'''def square (mylist):
  sq=[]
  for x in mylist:
    sq.append(x**2)
    return sq
li=[3,5,6]
result = square(li)
print("square of the list:",result)'''



'''
def findSquare(num):
    return num*num
print(findSquare(23))'''