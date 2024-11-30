myfile = open(
    r"C:\Users\Rajesh Sapehia\OneDrive\Desktop\file handling.txt", "a ")
for i in range(3):
    name = input("enter your name")
    myfile.write(name)
    myfile.write('\n')
myfile.close()
myfile = open(
    r"C:\Users\Rajesh Sapehia\OneDrive\Desktop\file handling.txt", "r")
print(myfile.append())
