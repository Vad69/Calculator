# Addition
# Substraction
# Division 
# Multiplication 
# Modular Division 
# Floor Division 
# Exponential 

# For addition
def addition (num1,num2):
    return num1 + num2

# For Substraction
def substraction (num1,num2):
    if (num1>num2):
       return num1-num2
    else:
       return num2-num1

# For Division
def division (num1,num2):
    if num1>num2:
       return num1/num2
    else:
       return num2/num1

# For Multiplication
def multiply (num1,num2):
    return num1*num2

# For exponential
def expo (num1,num2):
    return num1**num2

# For floor division
def floor (num1,num2):
    return num1//num2

# For modular division
def mod (num1,num2):
    return num1%num2

print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n" \
        "5. MOdular Divison\n" \
        "6. Floor Division\n" \
        "7. Exponential\n")

select=int(input("Enter your choice"))
num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))

if select==1:
     print(num1, "+", num2, "=", addition(num1, num2))
elif select==2:
     print(num1, "-", num2, "=", substraction(num1, num2))
elif select==3:
     print(num1, "*", num2, "=", multiply(num1, num2))
elif select==4:
     print(num1, "/", num2, "=", division(num1, num2))
elif select==5:
     print(num1, "%", num2, "=", mod(num1, num2))
elif select==6:
     print(num1, "//", num2, "=", floor(num1, num2))
elif select==7:
     print(num1, "**", num2, "=", expo(num1, num2))
else:
     print("Wrong Input")
