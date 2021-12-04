f = open("test.txt", "r")
lines = f.readlines()
f.close()
horizontalPos = 0
verticalPos = 0

for line in lines:
    (direction, steps) = line.split()
    if direction == "forward":
        horizontalPos += int(steps)
    if direction == "down":
        verticalPos += int(steps)
    if direction == "up":
        verticalPos -= int(steps)

print(horizontalPos * verticalPos)
