from operator import contains
import re
from unicodedata import name

def run():
    proceed = True
    bases = LoadOthers()
    roots = LoadRoots()
    endings = LoadEndings()
    while proceed:
        output = ""
        _input = input("Enter a short or a full name:  ")
        if len(_input) <= 6:
            count = []
            temp = re.split('([A-Z0-9])', _input)
            inputlist = list(filter(None, temp))
            for i in range(0, len(inputlist)):
                if inputlist[i].islower():
                        inputlist[i-1] = inputlist[i-1]+inputlist[i]
                        if i > 1:
                            count.append(i-1)
                        else:
                            count.append(i)
            for value in count:
                inputlist.pop(value)

            evalue = 0;

            if len(inputlist) == 2: 
                for base in bases:
                    if base["short"] == inputlist[1]:
                        output += base["iname"]+" "
                        evalue = base["enum"]
                for root in roots:
                    if root["short"] == inputlist[0]:
                        output += root["root"]
                output += endings[abs(evalue)-1]
                print(output)

            if len(inputlist) == 3:
                if inputlist[2].isnumeric():
                    for base in bases:
                        if base["short"] == inputlist[1]:
                            output += base["iname"]+" "
                            evalue = base["enum"]*int(inputlist[2])
                    for root in roots:
                        if root["short"] == inputlist[0]:
                            output += root["root"]
                            break
                    output += endings[abs(evalue)-1]
                    print(output)
                if inputlist[1].isnumeric():
                    for base in bases:
                        if base["short"] == inputlist[2]:
                            output += base["iname"]+" "
                            evalue = base["enum"]
                    for root in roots:
                        if root["short"] == inputlist[0]:
                            output += root["root"]
                    output += endings[int(abs((evalue))/int(inputlist[1]))-1]
                    print(output)

            if len(inputlist) == 4:
                for base in bases:
                    if base["short"] == inputlist[2]:
                        output += base["iname"]+" "
                        evalue = base["enum"]*int(inputlist[3])
                for root in roots:
                    if root["short"] == inputlist[0]:
                        output += root["root"]
                output += endings[int(abs(evalue/int(inputlist[1])))-1]
                print(output)
        if len(_input) > 6:
            tempending = 0
            tempnum = 0
            tempshort = ""
            temp = _input.split()
            for base in bases:
                if base["iname"].lower() == _input[0].lower():
                    tempnum = int(abs(base["enum"]))
                    tempshort = base["short"]
                    break
            for root in roots:
                if _input[1].lower().__contains__(root["root"].lower()):
                    output += root["short"]
                    break
            for i in (0, len(endings)-1):
                if _input[1].lower().__contains__(endings[i]):
                    tempending = i+1
                    break
            





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


run()