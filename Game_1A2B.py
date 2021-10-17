import random
from GUI.GUI import *

"""
1A2B Game 

A game that guess four-digit number

Status Code:
-1  : input length illegal
0   : the answer is not right, game should continue
1   : the answer is right, game pass

"""
class Game():
    def __init__(self):
        self.rndNum = random.randint(1000,9999)
        self.A = 0
        self.B = 0
    
    def start(self,guessNum):
        self.A , self.B = 0,0
        strNum = str(self.rndNum)
        if(len(guessNum) != 4 or str(guessNum).isdigit() != True):
            return -1
        else:
            for k in range(4):
                if guessNum[k] == strNum[k]:
                    self.A+=1
                    tempGuess = list(guessNum)
                    tempStr = list(strNum)
                    tempGuess[k] = '@'
                    tempStr[k] = '!'
                    guessNum = ''.join(tempGuess)
                    strNum = ''.join(tempStr)
            for i in range(4):
                for j in range(4):
                        if guessNum[i] == strNum[j]:
                            self.B+=1 
                            tempGuess = list(guessNum)
                            tempStr = list(strNum)
                            tempGuess[i] = '@'
                            tempStr[j] = '!'
                            guessNum = ''.join(tempGuess)
                            strNum = ''.join(tempStr)
            if  self.A == 4:
                return 1
            else:
                return 0
            

    def returnAnswer(self):
        answer = '答案:' + str(self.rndNum)
        return answer

    def reset(self):
        self.rndNum = random.randint(1000,9999)
        self.A = 0
        self.B = 0