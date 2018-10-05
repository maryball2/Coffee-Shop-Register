'''
Title: Coffee Shop For Mr.Nuckols
Author: Riley Carpenter, Erika Beneke, Bosah Mbajekwe
'''






import time
import decimal
import sys
import os





global fullcharge
global largecharge
global medcharge
global smallcharge
global totallarge
global totalmed
global totalsmall
global clearorcls





if sys.platform == "linux" or sys.platform == "posix":
    clearorcls = "clear"
else:
    clearorcls = "cls"
large = 2.0
medium = 1.9
small = 1.75
fullcharge = 0
largecharge = 0
medcharge = 0
smallcharge = 0
totallarge = 0
totalmed = 0
totalsmall = 0
decimal.getcontext().prec=8
global done
done = False
dayofweek = time.ctime()[0:3]
currenthour = time.ctime()[11:13]








def manyspace():
    global clearorcls
    os.system(clearorcls)
        
        
        
        
        
        
        
        
        
def menu():
	print("""
	Small Drink (9oz) = $1.75
	Medium Drink (12oz) = $1.90
	Large Drink (15oz) = $2.00
	""")
def largecalc():
	global large
	global medium
	global small
	global done
	global fullcharge
	global largecharge
	global medcharge
	global smallcharge
	global totallarge
	global totalmed
	global totalsmall
	quantitity = float(input("How many do you want "))
	fullcharge = fullcharge + (large * quantitity)
	largecharge = largecharge + (large * quantitity)
	totallarge += quantitity
	
	
	
	
	
	
	
	
	
def medcalc():
	global large
	global medium
	global small
	global done
	global fullcharge
	global largecharge
	global medcharge
	global smallcharge
	global totallarge
	global totalmed
	global totalsmall
	quantitity = float(input("How many do you want "))
	fullcharge = fullcharge + (medium * quantitity)
	medcharge = medcharge + (medium * quantitity)
	totalmed += quantitity
	
	
	
	
	
	
	
	
	
def smallcalc():
	global large
	global medium
	global small
	global done
	global fullcharge
	global largecharge
	global medcharge
	global smallcharge
	global totallarge
	global totalmed
	global totalsmall
	quantitity = float(input("How many do you want "))
	smallcharge = smallcharge + (small * quantitity)
	fullcharge = fullcharge + (small * quantitity)
	totalsmall += quantitity
	
	
	
	
	
	
	
	
	
	
def firstprogram():
	global done
	global fullcharge
	global largecharge
	global medcharge
	global smallcharge
	global totallarge
	global totalmed
	global totalsmall
	global large
	global medium
	global small
	fullcharge = 0
	largecharge = 0
	medcharge = 0
	smallcharge = 0
	totallarge = 0
	totalmed = 0
	totalsmall = 0
	done = False
	manyspace()
	print("Welcome to Riley's Reverse Mortgages Coffee Shop")
	print("When done ordering type Done, if you want to see a menu type Menu")
	while done == False:
		size = input("What size do you want (Small, Medium, or Large)")
		if size == "Done" or size == "done" or size == "d" or size == "D":
			done = True
		elif size == "Menu" or size == "menu" or size == "m" or size == "M":
			menu()
		else:
			
			if size == "Large" or size == "large" or size == "l" or size == "L":
				largecalc()
			elif size == "Medium" or size == "medium" or size == "m" or size == "M":
				medcalc()
			elif size == "Small" or size == "small" or size == "S" or size == "s":
				smallcalc()
			else:
				print("That's not a real size please try again")
				time.sleep(3)
			manyspace()
			secondprogram()
			
			
			
			
			
			
			
def secondprogram():
	global done
	global fullcharge
	global largecharge
	global medcharge
	global smallcharge
	global totallarge
	global totalmed
	global totalsmall
	global large
	global medium
	global small
	done = False
	manyspace()
	while done == False:
		print("Do you want another drink? If not type Done or type Menu to see a menu")
		size = input("What size do you want (Small, Medium, or Large)")
		if size == "Done" or size == "done" or size == "d" or size == "D":
			done = True
		elif size == "Menu" or size == "menu" or size == "m" or size == "M":
			menu()
		else:
			if size == "Large" or size == "large" or size == "l" or size == "L":
				largecalc()
			elif size == "Medium" or size == "medium" or size == "m" or size == "M":
				medcalc()
			elif size == "Small" or size == "small" or size == "S" or size == "s":
				smallcalc()
			else:
				print("That's not a real size please try again")
				time.sleep(3)
			manyspace()
	else:
		manyspace()
		print("The full price is $" + str("{0:.2f}".format(fullcharge)))
		print("The total price for",int(totallarge),"large drinks is $" + str("{0:.2f}".format(largecharge)))
		print("The total price for",int(totalmed),"medium drinks is $" + str("{0:.2f}".format(medcharge)))
		print("The total price for",int(totalsmall),"small drinks is $" + str("{0:.2f}".format(smallcharge)))
		input("Press enter when done reviewing your order")
		manyspace()
		
		
		
		
		
		
while dayofweek == "Sun":
	print("The Shop is currently closed, please come back later")
	time.sleep(1)
	manyspace()
while int(currenthour) < 5 or int(currenthour) > 20:
	print("The Shop is currently closed, please come back later")
	time.sleep()
	manyspace()
	
	
	
	
	
firstprogram()
while dayofweek != "Boi":
	while dayofweek == "Sun":
		print("The Shop is currently closed, please come back later")
		time.sleep(1)
		manyspace()
	while int(currenthour) < 5 or int(currenthour) > 20:
		print("The Shop is currently closed, please come back later")
		time.sleep()
		manyspace()
	waittime = 5
	while waittime != 0:
		print("Next Customer wait",waittime,"seconds to order")
		time.sleep(1)
		waittime -= 1
		manyspace()
	manyspace()
	firstprogram()
