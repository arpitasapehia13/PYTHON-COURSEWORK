from re import I


def factorial(x):
    fact = 1
    print("entered the number is:" , x)
    for i in range (1 , x+1):
        fact = fact * i
    print("factorial of", x , "is" ,fact)

number = eval(input("enter the number:"))
factorial(number)