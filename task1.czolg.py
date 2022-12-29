from array import *
import random

print("\nagar.czolg.io\nautorzy: Khulan Erdenebayar, Karol Kubek, Monika Halek, Patryk Podgórski , Krystyna Bodziony \npunkty:  \n")

def change(n, A): #losuje dwie wartości w zakresie planszy i zamienia puste pole na X
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

def print_board(A): #drukuje plansze 
   for r in A:
      for c in r:
         print(c,end = " ")
      print()

   print()

   
A = [[" . "]*11 for i in range(11)]

A[5][5]=" # "

A[2][3]=" X "
A[7][8]=" X "
A[4][0]=" X "
A[1][8]=" X "
A[3][2]=" X "
A[5][10]=" X "
A[0][9]=" X "
A[9][3]=" X "
A[10][5]=" X "

print_board(A)
