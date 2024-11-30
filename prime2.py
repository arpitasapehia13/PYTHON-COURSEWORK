def prime(num):
    if (num <= 1):
        return "Non-Prime"
    
    for i in range(2, int(num ** 1/2)):
        if (num % i == 0):
            return "Non-Prime"
            
    return "Prime"

num = int(input())
print(prime(num))