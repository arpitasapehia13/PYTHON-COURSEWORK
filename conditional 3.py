classes = int(input("enter number of classes held"))
attended = int (input("enter number of classes attended"))
percent = (attended/classes)*100

if(percent >= 75):
     print ("eligble for test" , percent)

