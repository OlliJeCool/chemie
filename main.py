import re
import loadFuncs as lf
import names as nm

def main():
    while True:
        if len(nm._input) <= 7:
            nm.fromFormulaToName()
        if len(nm._input) > 8:
            nm.fromNameToFormula()
        
main()