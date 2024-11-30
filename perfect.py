def perfect_no(n):
    sum = 0
    for x in range(1,n):
        if (n%x==0):
            sum += x
    return sum == n

a = eval(input("enter the no. to be checked"))
print(perfect_no(a))