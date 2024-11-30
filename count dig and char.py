myfile = open(
    r"C:\Users\Rajesh Sapehia\OneDrive\Desktop\file handling.txt", "r")
str1 = myfile.read()
print(str1)
count1 = 0
for i in str1:
    if (i.isupper()) == True:
        count1 += 1
print("the count of upper case letter is", count1)
