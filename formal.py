#formal

'''
def my_function(*formal):
	print(type(formal))
	s=0
	for x in formal:
		s=s+x
	print("Sum is ",s)
my_function(10,20)
my_function(10,20,30,40,50)
my_function(10.2,15.5,26.3)'''

#area

'''def area(r):
	return  (3.14*r**2)
def circumference(r):
	return (2*3.14*r)
radius=int(input("Enter the radius : "))
print("Area is ",area(radius))
print("Circumference is ",circumference(radius))'''

'''def func(x,ans):
	if(x==0):
		return 0
	else:
		return func(x-1,x+ans)
print(func(2,66))'''

#sum and avg
'''def sum(*no):
	print(type(no))
	s=0
	for x in no:
		s=s+x
	return s
def add(p):
	print(p*6)
def avg(s):
	print(s/5)
sm=sum(10,20,30,40)
add(sm)
sm=sum(25,36,45,78,52)
avg(sm)'''

#inteerest
'''def interest(x,y,z):
	i=x*y*z/100
	return i
p=int(input("Enter the principle amount : "))
r=int(input("Enter the rate of interest : "))
t=int(input("Enter the period : "))
i=interest(p,r,t)
print("Simple Interest is : ",i)'''


#simple_interest

'''ef simple_interest(p,t,r=5):
	i=p*r*t/100
	return i
principle_amount=int(input("Enter the principle amount : "))
time_period=int(input("Enter the time duration : "))
rate_of_interest=int(input("Enter the rate of interest : "))
i1=simple_interest(principle_amount,time_period)
print("Interest : ",i1)
i2=simple_interest(principle_amount,time_period,rate_of_interest)
print("Interest : ",i2)'''


