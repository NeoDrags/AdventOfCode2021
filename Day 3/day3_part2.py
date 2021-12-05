oxygen = ""
carbon_dioxide = ""
f = open("test.txt", "r")
oxygenLines = f.readlines()
f.close()
g = open("test.txt", "r")
carbon_dioxideLines = g.readlines()
g.close()
zeroCount = 0
oneCount = 0

for i in range (0, len(oxygenLines[0])):
    removeLines = []
    for line in oxygenLines:
        if line[i] == "0":
            zeroCount += 1
        else:
            oneCount += 1
    if zeroCount > oneCount:
        oxygen += "0"
    if zeroCount <= oneCount:
        oxygen += "1"
    for line in oxygenLines:
        if line[i] != oxygen[i] and len(oxygenLines) != 1:
            removeLines.append(line)
    oxygenLines = list(set(oxygenLines) - set(removeLines))
    zeroCount = 0
    oneCount = 0

for i in range (0, len(carbon_dioxideLines[0])):
    removeLines = []
    for line in carbon_dioxideLines:
        if line[i] == "0":
            zeroCount += 1
        else:
            oneCount += 1
    if zeroCount > oneCount:
        carbon_dioxide += "1"
    if zeroCount <= oneCount:
        carbon_dioxide += "0"
    for line in carbon_dioxideLines:
        if line[i] != carbon_dioxide[i] and len(carbon_dioxideLines) != 1:
            removeLines.append(line)
    carbon_dioxideLines = list(set(carbon_dioxideLines) - set(removeLines))
    zeroCount = 0
    oneCount = 0

oxygen_value= int(oxygenLines[0] , 2)
carbon_dioxide_value = int(carbon_dioxideLines[0], 2)
print(oxygen_value * carbon_dioxide_value)
