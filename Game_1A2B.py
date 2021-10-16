import random
from GUI.GUI import *

#1A2B Game
global rndNum
rndNum = random.randint(1000,9999)
def Game(guessNum):
    A,B = 0,0
    strNum = str(rndNum)
    returnAnswer()

    if(len(guessNum) != 4):
        return None,None,-1
    else:
        for k in range(4):
            if guessNum[k] == strNum[k]:
                A+=1
                tempGuess = list(guessNum)
                tempStr = list(strNum)
                tempGuess[k] = '@'
                tempStr[k] = '!'
                guessNum = ''.join(tempGuess)
                strNum = ''.join(tempStr)
        for i in range(4):
            for j in range(4):
                    if guessNum[i] == strNum[j]:
                        B+=1 
                        tempGuess = list(guessNum)
                        tempStr = list(strNum)
                        tempGuess[i] = '@'
                        tempStr[j] = '!'
                        guessNum = ''.join(tempGuess)
                        strNum = ''.join(tempStr)
        if  A == 4:
            return A,B,1
        else:
            return A,B,0
        

def returnAnswer():
    result = '答案:' + str(rndNum)
    return result

def reset():
    rndNum = random.randint(1000,9999)