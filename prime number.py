def prime(n):
        if(n==1):
            return "not a prime"
        elif(n==2):
            return "prime"
        else:
            for x in range(2,n+1):
                if(n%x==0):
                    return "not prime"
                else:
                    return "prime"
a = eval(input("enter a no. to check"))
prime(a)




    
