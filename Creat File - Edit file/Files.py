file = open("file.txt", "r")

#print(file.read())
#print(file.readlines()[2])
#print(file.readline())
#print(file.readline())
#print(file.readline())
#print(file.readline())

for line in file.readlines():
    print(line)
file.close()