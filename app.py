import addition
import subtraction
import multiplication
import division

#present user with 4 selections
print("Select your calculation")
print("1.Add two numbers")
print("2.Subtract two numbers")
print("3.Multiply two numbers")
print("4.divide two numbers")

while True:
    choice = input("Enter your choice (1/2/3/4) ")
    if choice in ("1","2","3","4"):
        num1 = float(input("Enter first number here "))
        num2 = float(input("Enter second number here "))

        if choice == "1":
            print(num1, "+", num2, "=", addition.addTwoNumbers(num1, num2))
        
        elif choice == "2":
            print(num1, "-" , num2 , "=" , subtraction.subtractTwoNumbers(num1, num2))
        
        elif choice == "3":
            print(num1, "*", num2,  "=",  multiplication.multiplyTwoNumber(num1, num2))
        
        elif choice == "4":
            print(num1, "/" , num2 , "=" , division.divideTwonumbers(num1, num2))
    
    else:
        ("its broken")
    
