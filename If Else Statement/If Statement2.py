num1 = float(input("Entre a number A: "))
operation = input('Entre an operation: "+" , "-" , "*" , "/": ')
num2 = float(input("Entre a number B: "))

if operation == "+":
    print(num1+num2)

elif operation =="-":
    print(num1-num2)

elif operation == "*":
    print(num1*num2)

elif operation == "/":
    country = input("What's your country: ")
    Country = "Tunisia"
    if country == Country:
        print(round((num1/num2),3))

    else:
        print(num1 / num2)
else:
    print("Please Entre a valid 'operation'")