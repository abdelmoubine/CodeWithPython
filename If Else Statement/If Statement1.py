def max():
    print("Welcome To Max number")
    num1 = input("Entre A number: ")
    num2 = input("Entre B number: ")
    num3 = input("Entre C number: ")

    if num1>=num2 and num1>=num3:
        print(num1 + " is bigger")
        return "Thank you for using our application"

    elif num2>=num1 and num2>=num3:
        print(num2 + " is bigger")
        return "Thank you for using our application"

    else:
        print(num3+ " is bigger")
        return "Thank you for using our application"
print(max())