n=input("Enter a number : ")
l=len(n)
n=int(n)
s=0
t=n
while n!=0:
	d=n%10
	s=s+d**l
	n=n//10
if t==s:
	print("Amstrong")
else:
	print("Not an amstrong")