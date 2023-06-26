a = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15) 
even , odd = 0,0
for num in a:
    if num % 2 == 0 :
        even+=1
    else:
        odd+=1
print("odd number:",odd)
print("even number:",even)