# Write a Python calculator that can perform: addition, subtraction, division, multiplication and modulus operations. It should accept user input
#Name: Akande Oluwatosin 

# state of purpose of the calculator
print("This is a simple calculator that can perform addition, subraction, division, multiplaction and modulus of two numbers")

print("Enter 1 for Addition ")
print("Enter 2 for Subtraction")
print("Enter 3 for Division")
print("Enter 4 for Multiplicaion")
print("Enter 5 for Modulos Operation")

# Addition Operation
def addition(a,b):
    return a + b

#Subtraction Operation
def subtraction(a,b):
    return a - b

#Division Operation
def division(a,b):
    return a / b

#Multiplication Operation
def multiplication(a, b):
    return a * b

#Modulus Operation
def modulus(a,b):
    return a % b


#Condition to know which operation to run
while True:
    # the input to know which operation to carry out
    x = input("input 1 ,2 3, or 4 for the operation you want to perform: ")
    
    #checking for value in the tuple to ascertain the condition
    if x in ("1", "2", "3", "4"):
        # a: input 1
        # b: input 2
        a = float(input("enter your first number: "))
        b = float(input("enter your second number: ")) 
        
        if x == "1":
            print(f"{a} + {b} = ", addition(a,b))
        elif x == "2":
            print(f"{a} - {b} = ", subtraction(a, b))
        elif x == "3":
            print(f"{a} / {b} = ", division(a, b))
        elif x == "4": 
            print(f"{a} * {b} = ", multiplication(a, b))
        elif x == "5":
            print((f"{a} % {b} = ", modulus(a, b) ))
        #condition to continue the loop
        Y = input("do you want to perform another operation, enter yes or no?  ")
        # convert Y into lower case to avoid bugs in the code
        y = Y.lower()
        if y == "no":
            print("thank you, come once again when you want to do basic arithemetic")
            break
            
    else: 
        print("invalid input, please enter a valid input")
    
    
    
    



