f = open("test.txt", "r")
lines = f.readlines()
f.close()
current = 0
currentLine = 0
count = 0

for line in lines:
    if currentLine == 0:
       current = int(line)
    if int(line) > current:
        count+= 1
        current = int(line)
    if int(line) <= current:
        current = int(line)
    currentLine+=1

print(count)
