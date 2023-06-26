#Binary to Decimal


'''def binaryToDecimal(binary):
 d=0
 for i in binary:
  d=d*2+int(i)
 return d
binary ="1010"
d=binaryToDecimal(binary)
print(d)
binaryToDecimal(binary)'''


#Decimal to Binary
 

def decimal_to_binary(decimal):
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return binary
decimal = 10
binary = decimal_to_binary(decimal)
print(binary)