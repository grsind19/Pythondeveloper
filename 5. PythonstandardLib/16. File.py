myfile = open("scores.txt","w")

print("name", myfile.name)
print("mode is", myfile.mode)

myfile.write("GBJ:100\nKHD: 55\nBB:89")
myfile.close()

myFile = open("scores.txt","r")

# print("Reading ..."+myFile.read())

print("First line" +myFile.readline())

for line in myFile:
  print(line)


myFile.close()