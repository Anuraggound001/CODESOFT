print("i can help you in mathematics operation")

def add(x,y):
    return x + y 
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y != 0:
        return x/y
    else:
        return "cannat divide by zero"

def calculator():

    num1 = float(input("enter the first number: "))
    num2 = float(input("enter the second number: "))

    print("Choose an operation: ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice  = input("Enter the operation number (1/2/3/4): ")

    if choice == '1':
        print(f"The result of addition is: {add(num1,num2)}")
    elif choice == '2':
        print(f"The result of subtraction is: {subtract(num1,num2)}")
    elif choice == '3':
        print(f"The result of multiplication is: {multiply(num1,num2)}")
    elif choice == '4':
        print(f"The result of division is: {divide(num1,num2)}")
    else:
        print("Invalid choice! Please select a valid operation.")

calculator()
