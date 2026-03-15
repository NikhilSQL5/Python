file = open("hello.txt", "r")

#readFile = file.read() #read entire txt file
#readFile = file.read(5) #specific lenth of charectors
#print(readFile)

line1 = file.readline() #print the 1st line
print(line1)

line2 = file.readline() #print the 2nd line
print(line2)


file.close()
