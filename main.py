def add(num1,num2):
   print(f"number1 + number2 = {num1 + num2}")

def subtract(num1,num2):
   print(f"number1 - number2 = {num1 - num2}")

def multiply(num1,num2):
   print(f"number1 * number2 = {num1 * num2}")

def divide(num1,num2):
   print(f"number1 / number2 = {num1 / num2}")  

def calculator():
   num1 = int(input("please enter your first number \n"))
   num2 = int(input("please enter your second number \n"))  
   operator = input("please enter the operator \n")  

   if operator == "+":
     add(num1,num2)
   elif operator == "-":
     subtract(num1,num2)
   elif operator == "*":
     multiply(num1,num2)
   elif operator == "/":
     divide(num1,num2)  
   else:
    print("invalid! please try again...")  

calculator()