import random
guessesTaken = 0
number = random.randint(1, 100)
print('Guess a number between 1 and 100 in 6 guesses.')
while guessesTaken < 6:
	print('Guess.') 
	guess = input()
	guess = int(guess)
	guessesTaken+=1
	if guess < number:
		print('Your guess is too low.') 
	if guess > number:
		print('Your guess is too high.')
	if guess == number:
		break
if guess == number:
	print('Good job! You guessed the number')
if guess != number:
	number = str(number)
	print('Nope. The number was ' + number)

