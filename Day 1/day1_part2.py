f = open("test.txt", "r")
lines = list(map(int, f.readlines()))
f.close()
current = 0
currentLine = 0
count = 0
Sum = 0

for i in range(0, len(lines) - 2):
    tempSum = sum(lines[i:i+3])
    if count == 0:
        Sum = tempSum
    if Sum < tempSum:
        count+=1
        Sum = tempSum
    if Sum >= tempSum:
        Sum = tempSum

print(count)
