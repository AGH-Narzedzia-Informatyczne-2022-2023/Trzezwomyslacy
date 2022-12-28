from array import *

print("\nagar.czolg.io\nautorzy: Khulan Erdenebayar, Karol Kubek, Monika Halek, Patryk Podgórski , Krystyna Bodziony \npunkty:  \n")

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

for r in A:
   for c in r:
      print(c,end = " ")
   print()
