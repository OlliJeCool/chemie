import loadFuncs as lf
import re

bases = lf.LoadOthers()
roots = lf.LoadRoots()
endings = lf.LoadEndings()


def fromNameToFormula(_input):
    output = ""
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

def fromFormulaToName(_input):
        for reg in lf.loadRegex():
            if re.match(reg["reg"], _input):
                if reg["num"] != 1:
                    match = True
                    temp = lf.GetFormula(_input)
                    nums = []
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
                    break
                else:
                    temp = lf.GetFormula(_input)
                    nums = []
                    evalue = 0
                    if temp[1].isnumeric() and temp[3].isnumeric() and temp[5].isnumeric():
                        nums.insert(0,int(temp[1]))
                        nums.insert(1,int(temp[3]))
                        nums.insert(2,int(temp[5]))
                    elif temp[1].isnumeric and temp[3].isnumeric():
                        nums.insert(0,int(temp[1]))
                        nums.insert(1,int(temp[3]))
                        nums.insert(2,1)
                    elif temp[1].isnumeric() and temp[4].isnumeric():
                        nums.insert(0,int(temp[1]))
                        nums.insert(1,1)
                        nums.insert(2,int(temp[4]))
                    elif temp[2].isnumeric() and temp[4].isnumeric():
                        nums.insert(0,1)
                        nums.insert(1,int(temp[2]))
                        nums.insert(2,int(temp[4]))