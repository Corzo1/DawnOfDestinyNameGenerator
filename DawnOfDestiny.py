def inputParse(userInput):
    userInputParsed = 0
    iVar2 = 0

    for cVar1 in userInput:
        iVar3 = iVar2 + 5
        userInputParsed ^= (ord(cVar1) & 0xFF) << (iVar2 & 0x1F)
        iVar2 = iVar3 if iVar3 < 0x18 else iVar2 - 0x13

    return userInputParsed & 0xFFFFFFFF


def get_mhr_file(parsedVariable):
    parsedVariable = (parsedVariable >> 6) % 3

    if parsedVariable == 1:
        pcVar4 = "Zera deck"
    elif parsedVariable == 2:
        pcVar4 = "Cosmo Queen deck"
    else:
        pcVar4 = "Tri-Horn Dragon Deck"

    return pcVar4


string = input("input: ")
result = inputParse(string)
print(result) 
print(get_mhr_file(result))


