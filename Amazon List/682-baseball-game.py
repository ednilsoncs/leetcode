# https://leetcode.com/problems/baseball-game/description/
from typing import List


def calPoints(ops: List[str]) -> int:
      pilha = [] 
      total = 0
      for value in ops:
        if(value == "C"):
          total = total - pilha[len(pilha)-1]
          pilha.pop()
      
        elif(value == "D"):
          total = (pilha[len(pilha)-1] * 2) + total
          pilha.append(pilha[len(pilha)-1] * 2)
        
        elif(value == "+"):
          total = pilha[len(pilha)-1] + pilha[len(pilha)-2] + total
          pilha.append(pilha[len(pilha)-1] + pilha[len(pilha)-2])

        else:
          pilha.append(int(value))  
          total =  int(value) + total
        
      return total   



print(calPoints(["5","2","C","D","+"]))