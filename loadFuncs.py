import re

def LoadRoots():
    elements = []
    with open("./roots.txt", "r", encoding="utf-8") as f:
        lines = [line.rstrip('\n') for line in f]
        for line in lines:
            temp = line.split(';')            
            elements.append({"num" : int(temp[0]), "short" : temp[1], "root" : temp[2]})
    return elements
 
def LoadOthers():
    bases = []
    with open("./placeholder.txt", "r", encoding="utf-8") as t:
        lines = [line.rstrip('\n') for line in t]
        for elements in lines:
            temp = elements.split(';')
            bases.append({"short" : temp[0], "name":temp[1], "enum": int(temp[2]), "iname" : temp[3]})
    return bases

def LoadEndings():
    endings = []
    with open("./koncovky.txt", "r" , encoding="utf-8") as t:
        temp = t.readline()
    endings = temp.split(";")
    return endings

def loadRegex():
    regex = []
    with open("./regex.txt", "r", encoding="utf-8") as t:
        temp = t.readlines()
        for num in range(0, len(temp)):
            temp[num] = temp[num].replace("\n", "")
        for reg in temp:
            tempnum = reg.split(";")
            regex.append({"num" : int(tempnum[0]), "reg" : tempnum[1]})
    return regex


def GetFormula(_input):
    count = []
    temp = re.split('([A-Z0-9])', _input)
    inputlist = list(filter(None, temp))
    for i in range(0, len(inputlist)):
        if inputlist[i].islower():
            inputlist[i-1] = inputlist[i-1]+inputlist[i]
            if len(count) > 0:
                count.append(i-1)
            else:
                count.append(i)
    for value in count:
        inputlist.pop(value)
    return inputlist