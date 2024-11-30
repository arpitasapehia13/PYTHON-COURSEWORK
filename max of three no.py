def max(x , y ,z):
    if( x>y>z or x>z>y):
        print("x is greater" , x)
    elif (y>x>z or y>z>x):
        print("y is greater" , y)
    else:
        print("z is greater" ,z)    