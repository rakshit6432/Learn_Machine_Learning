def isCryptSolution(crypt, solution):
    checkDict = dict(i for i in solution)
    newList = []

    for c in crypt:
        for k, v in checkDict.items():
            c = c.replace(k, v)
        newList.append(c)

    if (len(newList[0]) > 1):
        if ((newList[0][0] != '0') and (newList[1][0] != '0') and (newList[2][0] != '0')):
            return(eval('int(newList[0]) + int(newList[1]) == int(newList[2])'))
        else:
            return False
    else:
        return(eval('int(newList[0]) + int(newList[1]) == int(newList[2])'))


# A more optimized solution
def isCryptSolutionOptimized(crypt, solution):
    mapping = {ord(c): d for c, d in solution}
    *crypted, = map(lambda x: x.translate(mapping), crypt)
    zeroes = any(x != "0" and x.startswith("0") for x in crypted)
    equation = int(crypted[0]) + int(crypted[1]) == int(crypted[2])
    return not zeroes and equation
