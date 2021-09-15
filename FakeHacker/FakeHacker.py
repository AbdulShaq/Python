"""Fake Hacker typist program that will type out real code(in any language given by the
user in a .txt file) no matter what keys the user presses"""

# MCS 260 Fall 2020 Project 4
# Abdul Shaqildi
# Declaration: I, Abdul Shaqildi, am the sole author of this code, which
# was developed in accordance with the rules in the course syllabus.

import sys
from pynput import keyboard #this module is to get the necessary functions to monitor the keyboard
from colorama import Fore, init#This module is just for making certain text appear in a color

init(convert=True)

current= [] #list to keep track of what keys have been pressed wihtout a response

access_granted_times = [1,2,3] #limit of times access granted can be printed

#retrieve the code in a given text file, reads it and sorts each character and whitespace into a list
file = open(sys.argv[1], 'r')
f= file.read()
chara =[]
for character in f:
  chara.append(character)


def on_press(key):
      """This function is to carry out the tasks to print the next character e
      every time a key is pressed"""
      current.append(key) 
      
      for i in current:      
         s=""
         
         if len(chara) == 0:

           if len(access_granted_times) !=0: #as long as it has not printed access granted 3 times it will print
              print(" ")
              print(Fore.LIGHTGREEN_EX+'ACCESS GRANTED'.center(150,'='))
              access_granted_times.pop(0)

           else:
              exit()
               
         else: #here the elements of the list chara then are added to a string and update the text printed out for each element
          s=s+chara[0]
          print(s,end = '')
          chara.pop(0)#character just printed gets removed from chara

      current.pop(0) #key that just proccessed the next character is removed from current
       
    
with keyboard.Listener(on_press=on_press) as listener: #Listener is used to monitor for key presses only and then calling the on_press function to carry out what is needed when a key is pressed
    listener.join()