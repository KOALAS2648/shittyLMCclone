def readFile(code):
    codeFile = open(code, "r")
    codeLines = codeFile.readlines()
    codeLines = [i[:-1] if "\n" in i else i for i in codeLines]
    codeLines = [i.split(" ") for i in codeLines]
    codeLines = [i for i in codeLines if i[0] != "//"]
    codeLines = [i for i in codeLines if i[0] != '']
    return codeLines


labelsDict = {}
def getLabels(code, main_functions):
    for index, line in enumerate(code):
        if line[0] in main_functions:
            pass
        elif line[0] not in main_functions and line[1] != "DAT":
            labelsDict[line[0]] = index
            code[index].pop(0)

variablesDict = {}
def getVariables(code, main_functions):
    for index, line in enumerate(code):
        if line[0] in main_functions:
            pass
        elif line[0] not in main_functions and line[1] == "DAT":
            variablesDict[line[0]] = index
            code[index].pop(0)

code = readFile("g.txt")

main_functions = {"INP":901, "OUT":902, "HLT":"000", "STA":300, "DAT":"0", "BRA":600, "BRZ":700, "BRP":800, "ADD":100, "SUB":200, "LDA":500, "OTC":400}
drqInput = ["INP", "OUT", "HLT"]



loops = ["BRA", "BRP", "BRZ"]
memory = [0 for i in range(0,99)]

getLabels(code, main_functions)
getVariables(code, main_functions)
for index, line in enumerate(code):

    if line[0] in loops:
        labelname = line[-1]
        line[-1] = labelsDict[labelname]

    if line[-1] in variablesDict:
        varname = line[-1]
        line[-1] = variablesDict[varname]
    if line[0] == "OTC":
        memory[index] = main_functions["OTC"]
        continue
    if line[0] in main_functions:
        if line[0] in drqInput:
            memory[index] = main_functions[line[0]]
        else:
            memory[index] =main_functions[line[0]]+line[-1]
if __name__ == "__main__":
    print(memory)
    print(labelsDict)
    print(variablesDict)