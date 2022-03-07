import names as nm

def main():
    while True:
        _input = input("Enter a fromula or the whole name...  ")
        if len(_input) <= 7:
            print(nm.fromFormulaToName(_input))
        if len(_input) > 8:
            nm.fromNameToFormula(_input)
        
main()