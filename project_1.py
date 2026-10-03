num1=int(input("enter a value:"))
num2=int(input("enter b value:"))
operator=input("enter a operator:")

if operator=="+":
    print(f"adittion of 2 numbers is {num1+num2}")
elif operator=="-":
    print(f"substration of 2 numbers is {num1-num2}")
elif operator=="*":
    print(f"multiplication of 2 numbers is {num1*num2}")
else:
    print(f"division of 2 numbers is {num1/num2}")

