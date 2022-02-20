import re

def main():
    bases = LoadOthers()
    roots = LoadRoots()
    endings = LoadEndings()
    while True:
        output = ""
        _input = input("Enter a short or a full name:  ")
        if len(_input) <= 7:
            test(_input, bases, roots, endings)
            print(GetFormula(_input))
        if len(_input) > 6:
            tempending = 0
            tempnum = 0
            tempshort = ""
            temp = _input.split()
            for base in bases:
                if base["iname"].lower() == temp[0].lower():
                    tempnum = int(abs(base["enum"]))
                    tempshort = base["short"]
                    break
            for root in roots:
                if temp[1].lower().__contains__(root["root"].lower()):
                    output += root["short"]
                    temp[1] = temp[1].replace(root["root"].lower(), "")
            for i in range(0, len(endings)-1):
                if temp[1].lower() == endings[i]:
                    tempending = i+1
                    break
            finalending = ((tempending*tempnum)/tempending)
            finalnum = ((tempending*tempnum)/tempnum)
            output += str(int(finalending))+tempshort+str(int(finalnum))
            print(output)       


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
        for line in t:
            tempt = line.split(";")
            regex.append({"num" : tempt[0], "reg" : tempt[1]})
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

def test(_input, bases, roots, endings):
    for reg in loadRegex():
        if re.match(reg["reg"], _input):
            temp = GetFormula(_input)
            nums = []
            if reg["num"] != 1:
                evalue = 0
                output = ""
                if len(temp) == 4:
                    if temp[1].isnumeric() and temp[3].isnumeric():
                        nums.insert(0,int(temp[1]))
                        nums.insert(1,int(temp[3]))
                else:
                    if len(temp) == 2:
                        nums.insert(0,1)
                        nums.insert(1,1)
                    elif temp[1].isnumeric() and len(temp) == 3:
                        nums.insert(0,int(temp[1])) 
                        nums.insert(1,1)
                    elif temp[2].isnumeric() and len(temp) == 3:
                        nums.insert(0,1)
                        nums.insert(1,int(temp[2]))
            else:
                if temp[1].isnumeric() and temp[3].isnumeric() and temp[5].isnumeric():
                    nums.insert(0,int(temp[1]))
                    nums.insert(1,int(temp[3]))
                    nums.insert(2,int(temp[5]))
                elif temp[1].isnumeric and temp[3].isnumeric() and reg["num"] == 1:
                    nums.insert(0,int(temp[1]))
                    nums.insert(1,int(temp[3]))
                    nums.insert(2,1)
                elif temp[1].isnumeric() and temp[5].isnumeric() and reg["num"] == 1:
                    nums.insert(0,int(temp[1]))
                    nums.insert(1,1)
                    nums.insert(2,int(temp[5]))
                elif temp[3].isnumeric() and temp[5].isnumeric() and reg["num"] == 1:
                    nums.insert(0,1)
                    nums.insert(1,int(temp[3]))
                    nums.insert(2,int(temp[5]))
            for base in bases:
                if len(temp) != 2:
                    if temp[2] == base["short"]:
                        output += base["iname"]+" "
                        evalue = int(base["enum"])*nums[1]
                        break
                    elif temp[1] == base["short"]:
                        output += base["iname"]+" "
                        evalue = int(base["enum"])*nums[1]
                        break
                else:
                    if temp[1] == base["short"]:
                        output += base["iname"]+" "
                        evalue = int(base["enum"])*nums[1]
                        break
            for root in roots:
                if temp[0] == root["short"]:
                    output += root["root"]
                    break
            output+= endings[int(abs((evalue))/nums[0])-1]
            print(output)

main()