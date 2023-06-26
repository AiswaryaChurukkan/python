
# Function to convert decimal number
# to binary using recursion
a=input("enter")
def DecimalToBinary(num):
    print("Enter the number:",num)
    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end = '')
    return DecimalToBinary()    