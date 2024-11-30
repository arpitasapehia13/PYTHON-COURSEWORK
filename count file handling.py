myfile = open(
    r"C:\Users\Rajesh Sapehia\OneDrive\Desktop\file handling.txt", "r")
count = 0
str1 = myfile.read()
for i in str1:
    if (i == "a"):
        count = count+1
print("the frequency of letter a is", count)
