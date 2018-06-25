
# Tokenizer
# TODO: Add code to treat quoted code as one token
def tokenize(filepath):
    codeLines = [line.rstrip('\n') for line in open(filepath)]
    codeLinesTokens = []
    for line in codeLines:
        codeLinesTokens.append(line.split())
    return codeLinesTokens

# interpreter

#Varibles stored here
varibles = {}

def returnTrueValue(value):
    if value in varibles:
        return varibles[value]
    else:
        return value

def addWhiteSpace(value):
    value = value.replace("_", " ")
    return value
#Functions

def importFunction(functionPath, functionName):
    varibles[functionName] = functionPath

def callFunction(functionName):
    codeLinesTokens = tokenize(returnTrueValue(functionName))
    readCode(codeLinesTokens)

#Set Varibles
def setVar(var, value):
    varibles[var] = returnTrueValue(value)

def setVarToInput(var, i):
    setVar(var, input(addWhiteSpace(i)))

def newList(name):
    varibles[name] = []

#Print

def printVar(var):
    print(str(addWhiteSpace(returnTrueValue(var))))

#Concatenation

def addToVar(var, val):
    varibles[var] += returnTrueValue(val)

#Arithmitic

# Plus

def plusToVar(var,val):
    varInt = int(varibles[var])
    valueInt = int(returnTrueValue(val))
    sum = varInt + valueInt
    varibles[var] = str(sum)

# Subtract

def subtractFromVar(var,val):
    varInt = int(varibles[var])
    valueInt = int(returnTrueValue(val))
    n = varInt - valueInt
    varibles[var] = str(n)

def multiplyByVar(var,val):
    varInt = int(varibles[var])
    valueInt = int(returnTrueValue(val))
    n = varInt * valueInt
    varibles[var] = str(n)

# Divide

def divideByVar(var,val):
    varInt = int(varibles[var])
    valueInt = int(returnTrueValue(val))
    n = int(varInt / valueInt)
    varibles[var] = str(n)

# Control

# If Statement

def ifStatment(val1, comparator, val2, function):

    if val1 in varibles:
        val1 = varibles[val1]

    if val2 in varibles:
        val2 = varibles[val2]

    if comparator == "==":
        if val1 == val2:
            callFunction(function)
    elif comparator == ">":
        if val1 > val2:
            callFunction(function)
    elif comparator == "<":
        if val1 < val2:
            callFunction(function)
    elif comparator == "!=":
        if val1 != val2:
            callFunction(function)
    elif comparator == "=/":
        if val1 % val2 == 0:
            callFunction(function)
    elif comparator == "!/":
        if val1 % val2 != 0:
            callFunction(function)

def ifElseStatment(val1, comparator, val2, function, elseFunction):

    if val1 in varibles:
        val1 = varibles[val1]

    if val2 in varibles:
        val2 = varibles[val2]

    if comparator == "==":
        if val1 == val2:
            callFunction(function)
        else:
            callFunction(elseFunction)
    elif comparator == ">":
        if val1 > val2:
            callFunction(function)
        else:
            callFunction(elseFunction)
    elif comparator == "<":
        if val1 < val2:
            callFunction(function)
        else:
            callFunction(elseFunction)
    elif comparator == "!=":
        if val1 != val2:
            callFunction(function)
        else:
            callFunction(elseFunction)
    elif comparator == "=/":
        if val1 % val2 == 0:
            callFunction(function)
        else:
            callFunction(elseFunction)
    elif comparator == "!/":
        if val1 % val2 != 0:
            callFunction(function)
        else:
            callFunction(elseFunction)

# For Loop

def forLoop(low,high,function):
    for i in range(int(returnTrueValue(low)),int(returnTrueValue(high)) + 1):
        callFunction(function)
        if low in varibles:
            v = int(varibles[low]) + 1
            varibles[low] = str(v)
"""
def forEach(list,var, function):
    for value in list:
        varibles[var] = value
        callFunction(function)

def addToList(list, val):
    varibles[list].append(val)
"""
def readCode(codeLinesTokens):
    for line in codeLinesTokens:
        for token in line:
            if token == "=":
                setVar(line[0], line[2])
            elif token == "get_input":
                setVarToInput(line[1], line[3])
            elif token == "print":
                printVar(line[1])
            elif token == "append":
                addToVar(line[0], line[2])
            elif token == "+":
                plusToVar(line[0], line[2])
            elif token == "-":
                subtractFromVar(line[0], line[2])
            elif token == "*":
                multiplyByVar(line[0],line[2])
            elif token == "/":
                divideByVar(line[0],line[2])
            elif token == "import":
                importFunction(line[1], line[3])
            elif token == "call":
                callFunction(line[1])
            elif token == "if":
                ifStatment(line[1],line[2],line[3],line[5])
            elif token == "if_else":
                ifElseStatment(line[1], line[2], line[3], line[5], line[7])
            elif token == "for_range":
                forLoop(line[1],line[2],line[4])
            elif token == "new_list":
                newList(line[1])

codeLinesTokens = tokenize("main.dee")
readCode(codeLinesTokens)