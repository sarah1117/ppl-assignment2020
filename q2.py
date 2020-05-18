import random
min = 1
max = 6
ch = "Y"
while ch == "Y":	
	print("Rolling the dice...")
	print("The value is....")
	print(random.randint(min, max))
	ch = input("Roll the dices again?")

