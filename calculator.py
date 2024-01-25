# making a simple calculatorin python
print("Select a number to perform an opration : ")
print("1.Addition")   # add
print("2.subtraction")  # subtract
print("3.multiplication")  # multiply
print("4.divison") # divide

opration = input()
 
if opration == "1":
    num1 = input("enter a first number :")
    num2 = input("enter a second number :")
    print("the addition is :"+ str(int(num1)+int(num2)))
elif opration == "2":
    num1 = input("enter a first number :")
    num2 = input("enter a second number :")
    print("the subtraction is :"+ str(int(num1)-int(num2)))
elif opration == "3":
    num1 = input("enter a first number :")
    num2 = input("enter a second number :")
    print("the multiple is :"+ str(int(num1)*int(num2)))
elif opration == "4": 
    num1 = input("enter a first number :")
    num2 = input("enter a second number :")
    print("the divison is :"+ str(int(num1)/int(num2)))
    
       