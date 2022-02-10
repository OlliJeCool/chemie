import re
from numpy import void

from sqlalchemy import true


def Run():
    proceed = true
    while proceed:
        try:
            value = input("Enter a short or a full name")
            if len(value) <= 6:
                temp = re.findall('[A-Z][^A-Z]*', value)
                bases = LoadOthers()
                for items in temp:
                    if len(items) == 3 or len(items) == 2:
                        for chars in items:
                            if chars[3].isnumeric():
                                keep = int(chars)
                                items
            if len(value) > 6:
                temp = value.split()
        except:
            print("Vaule incorrect")
    return temp



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
