f = open("test.txt", "r")
lines = f.readlines()
f.close()
gamma = ""
epsilon = ""
zeroCount = 0
oneCount = 0

for i in range(0, len(lines[0])):
    for line in lines:
        if line[i] == "0":
            zeroCount += 1
        if line[i] == "1":
            oneCount += 1
    if zeroCount > oneCount:
        gamma += "0"
        epsilon += "1"
    if zeroCount < oneCount:
        gamma += "1"
        epsilon += "0"
    zeroCount = 0
    oneCount = 0

gammaValue = int(gamma , 2)
epsilonValue = int(epsilon, 2)
print(gammaValue * epsilonValue)
