# -*- coding: UTF-8 -*-
import os, sys

def refina(path):
   fina = os.listdir(path)
   return(fina)

def nain(fina):
   i = 1
   for item in fina:
      return(item)
      if i == len(fina):
         break;
      else:
         i+=1

if __name__ == "__main__":
   refina("lrc")
   print(nain(refina("lrc"))) 

