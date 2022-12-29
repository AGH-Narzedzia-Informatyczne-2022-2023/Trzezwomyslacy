from array import *
import random

print("\nagar.czolg.io\nautorzy: Khulan Erdenebayar, Karol Kubek, Monika Halek, Patryk Podgórski , Krystyna Bodziony \npunkty:  \n")

def change(n, A):
   for i in range(n):
      a = random.randint(0, 10)
      b = random.randint(0, 10)

      while(1):
         if(A[a][b] == " . "):
            A[a][b] = " X "
            break
         if(A[a][b] == " # " or A[a][b] == " X "):
            a = random.randint(0, 10)
            b = random.randint(0, 10)

def print_board(A): 
   for r in A:
      for c in r:
         print(c,end = " ")
      print()

   print()


A = [[" . "]*11 for i in range(11)]

n=1

A[5][5]=" # "
A[2][3]= change(n, A)
A[7][8]= change(n, A)
A[4][0]= change(n, A)
A[1][8]= change(n, A)
A[3][2]= change(n, A)
A[5][10]= change(n, A)
A[0][9]= change(n, A)
A[9][3]= change(n, A)
A[10][5]= change(n, A)

print_board(A)

