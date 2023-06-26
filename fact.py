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