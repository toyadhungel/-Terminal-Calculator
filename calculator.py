from ast import operator

#calculating 
def calculator():
    print("This is a command line calculator")
    operator = input(''' 
    + for add
    - for sub
    * for multiply 
    / for divide: \n''')

    nr1=float(input("Enter the first number: "))
    nr2=float(input("Enter the second number: "))

    if operator == '+':
        print(nr1 + nr2)
    elif operator =='-':
        print (nr1-nr2)
    elif operator =='*':
        print(nr1*nr2)
    elif operator =='/':
        print(nr1/nr2)
    else:
        print("invalid input, please enter correct operator")

    calcAgain()

# To calculate again base on user input
def calcAgain():
    print("Do you wanna calculate again? \n")
    answer=input("Enter Y/s for yes or N/n for no: \n" )

    if answer=='y':
        calculator()
    elif answer =='n':
        print("good bye, see you again")
    else:
        calcAgain()
            
calculator()#calling the function 
