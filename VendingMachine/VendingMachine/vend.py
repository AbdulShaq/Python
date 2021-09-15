"""A vending machine program that will read the products 
and keep count of credit and return change and product """
# MCS 260 Fall 2020 Project 2
# Abdul Shaqildi
# Declaration: I, Abdul Shaqildi, am the sole author of this code, which
# was developed in accordance with the rules in the course syllabus.
import sys

def read(file):
    """This function is to read the invintory file and store it into list"""
    File = open(file, "r")  
  
    inventory = []
      #this is where each line will be split up and then assigned into a dictionary
      #which then will be put into list 'inventory'
    for text in File:
        info = text.split(',')
        Dict = {'name':(str(info[2]).strip('\n')), 'stock':int(info[0]), 'price':(int(info[1])/100)}
        inventory.append(Dict)
    File.close()
    
    return inventory

def selection(s, credit):
 """This function is to read the the users selection and either add to the users credit by increments
   of 5 or vend the user selection if they have sufficent funds"""
 c = credit
 max= 0

 for i in inventory:
     if i['price'] > max:
         max = i['price']

 if select == "inventory":
        for i in inventory:
           print(inventory.index(i),i['name'],"${:}".format(format(i['price'], '.2f')),"({:} available)".format(i['stock']))
 elif select == "quarter":
     if c >= max:
         print("RETURN: quarter")
     else:
         c = c + .25

 elif select == "dime":
     if c >= max:
         print("RETURN: dime")
     else:
         c = c + .10

 elif select == "nickel":             
     if c >= max:  
         print("RETURN: nickel")
     else:
         c = c + .05001  #it is set to .05001 to account for the floats so it will round

 elif select == '0':
      if inventory[0]['stock'] == 0:
         print("MSG: Out of stock")
      elif c < inventory[0]['price']:
         print("MSG : Insufficient credit")
      else:
       print("VEND:", inventory[0]['name'])
       t= change(c - inventory[0]['price'])
       c = t
       inventory[0]['stock'] = inventory[0]['stock'] - 1

 elif select == '1':
      if inventory[1]['stock'] == 0:
         print("MSG: Out of stock")
      elif c < inventory[1]['price']:
         print("MSG : Insufficient credit")
      else:
        print("VEND:", inventory[1]['name'])
        t= change(c - inventory[1]['price'])
        c = t
        inventory[1]['stock'] = inventory[1]['stock'] - 1

 elif select == '2':
      if inventory[2]['stock'] == 0:
         print("MSG: Out of stock")
      elif c < inventory[2]['price']:
         print("MSG : Insufficient credit")
      else:
       print("VEND:", inventory[2]['name'])
       t= change(c - inventory[2]['price'])
       c = t
       inventory[2]['stock'] = inventory[2]['stock'] - 1
        
 elif select == '3':
      if inventory[3]['stock'] == 0:
         print("MSG: Out of stock")
      elif c < inventory[3]['price']:
         print("MSG : Insufficient credit")
      else:
       print("VEND:", inventory[3]['name'])
       t= change(c - inventory[3]['price'])
       c = t
       inventory[3]['stock'] = inventory[3]['stock'] - 1

 elif select == '4':
      if inventory[4]['stock'] == 0:
         print("MSG: Out of stock")
      elif c < inventory[4]['price']:
         print("MSG : Insufficient credit")
      else:
       print("VEND:", inventory[4]['name'])
       t= change(c - inventory[4]['price'])
       c = t
       inventory[4]['stock'] = inventory[4]['stock'] - 1

 elif select == '5':
     if inventory[5]['stock'] == 0:
         print("MSG: Out of stock")
     elif c < inventory[5]['price']:
         print("MSG : Insufficient credit")
     else:
      print("VEND:", inventory[5]['name'])
      t= change(c - inventory[5]['price'])
      c = t
      inventory[5]['stock'] = inventory[5]['stock'] - 1
 
 elif select == "return":
    t = change(c)
    c = t

 elif select == "restock" and num:
     x = num
     item = int(x[0])
     y = int(x[1])
     restock(item, y)

 elif select == "exit":
     sys.exit()
 return c

def change(c):
 """This function takes the remaining credit(if any) 
 and tell the user how much will be returned to them"""
 #each value compared in the while loops is .01 less than coin value to account for float number not rounding
 while c > 0.24:    
      print("RETURN: quarter")
      c = c-.25
 while c < .25 and c >.09: 
      print("RETURN: dime")
      c= c-.10
 while c < .10 and c > .04:
      print("RETURN: nickel")
      c = c-.05
 return 0

def restock(item, num):
    """This function is for restocking vending machine items"""
    inventory[item]['stock'] = inventory[item]['stock'] + num

#This passes the given inventory text file through the 'read' function 
#and then assigning the returned list to inventory
inventory = read("C:\\Users\\Abdul Shaqildi\\Desktop\\Code\\Python\\VendingMachine\\VendingMachine\\inventory.txt")
#initalizing the credit to zero so that the user must enter in coins
credit = 0

while True:   #This while loop is to consitantly keep prompting the user 
              #and updating their credit without going over most expensive item
 print("CREDIT: ${:.2f}".format((credit)))
 select, *num = input(">").split() #to take a string input then making integer inputs an option to put in for restock use
 credit = selection(select, credit)