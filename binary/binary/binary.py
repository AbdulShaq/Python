"""Calculate the binary digits of a given integer, n,  entered by the user"""
# MCS 260 Fall 2020 Project 1
# Abdul Shaqildi
# Declaration: I, Abdul Shaqildi, am the sole author of this code, which
# was developed in accordance with the rules in the course syllabus.

OrginalEntry = n = int(input())


print("x x//2 x%2")

binary = ""

while True:
   
   print(n, n//2, n%2)
   
   binary = str(n%2) + binary
   n = n//2
   if n == 0:
       break

print("Therefore,", OrginalEntry,"=", "0b" + binary)


