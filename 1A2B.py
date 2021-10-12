import numpy as np
import random

#1A2B Game
rndNum=random.randint(1000,9999)
print(rndNum)
while (1):
    A=0 
    B=0
    strNum=str(rndNum)
    guessNum=input("輸入猜測數值:")
    if(len(guessNum)!=4):
        print("請重新輸入數值!")
        continue
    else:
        for k in range(4):
            if guessNum[k]==strNum[k]:
                A+=1
                tempGuess=list(guessNum)
                tempStr=list(strNum)
                tempGuess[k]='@'
                tempStr[k]='!'
                guessNum=''.join(tempGuess)
                strNum=''.join(tempStr)
        for i in range(4):
            for j in range(4):
                    if guessNum[i]==strNum[j]:
                        B+=1 
                        tempGuess=list(guessNum)
                        tempStr=list(strNum)
                        tempGuess[i]='@'
                        tempStr[j]='!'
                        guessNum=''.join(tempGuess)
                        strNum=''.join(tempStr)
        if  A == 4:
            print("4 A 0 B,你猜對了!")
            break
        else:
            print(A,'A',B,'B')
