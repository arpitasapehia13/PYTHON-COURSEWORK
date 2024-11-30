Quantity = int(input("enter the quantity"))
cost = Quantity * 100
if(cost > 1000):
    print("discount of 10percent is given" , (cost - (cost*0.1)))