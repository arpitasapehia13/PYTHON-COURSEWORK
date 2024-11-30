counter = 0
psswrd = "ABC123"
x = input("enter the password")
for x in range(3):
    if (x == psswrd):
       print ("you have logged in")
    else:
        print ("failed")
        counter = counter + 1