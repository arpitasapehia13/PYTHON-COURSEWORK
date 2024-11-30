def range1 (x,y,n):
    print(x,y,n)
    for i in range (x,y+1):
        if (i==n):
            print(n)
        else:
            print("not in range")
range1(1,6,4)