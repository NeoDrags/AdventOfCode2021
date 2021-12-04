f = open("test.txt", "r")
lines = f.readlines()
f.close()
horizontalPos = 0
verticalPos = 0
aim = 0

for line in lines:
    (direction, steps) = line.split()
    if direction == "forward":
        horizontalPos += int(steps)
        verticalPos += int(steps) * aim  
    if direction == "down":
        aim += int(steps)
    if direction == "up":
        aim -= int(steps)

print(horizontalPos * verticalPos)
