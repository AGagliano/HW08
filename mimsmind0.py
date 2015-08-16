#!/usr/bin/env python

################################################################################

#Imports
import random
import sys

#Body
def determine_digits():
	'''Retrieves the number of digits from an arg given in the command line.
	If an arg is not given, the number of digits defaults to 1.

	Function returns the number of digits.
	'''
	try:
		digits = int(sys.argv[1])			
	except:
		digits = 1
	#Convert digit to default of 1, if user input is not applicable.
	if type(digits) is str or digits <=0:
		digits = 1

	return digits

def generate_random_number(digits):
	'''Generates a random positive integer with the number of digits (d)
	passed to the function. Returns the random positive integer.
	'''
	number = random.randint(0, (10**digits)-1)	
	return number	

def user_guesses(digits):
	'''Function promprts user to guess a positive integer, 
	and will prompt the user again if the input they 
	provide is not appropriate (i.e. a string, a negative number, 
	or a number with too many digits).
	'''
	#Set pluralization of 'digits' for prompting user.
	if digits == 1:
		digits_plural = ''
	else:
		digits_plural = 's'

	#Prompt user to guess a positive integer. 
	#Prompts user again if input is not an appropriate guess.
	while True:
		guess = raw_input('Guess a positive integer with {0} digit{1}.\n>'.format(digits, digits_plural))
		if len(guess) != digits or '.' in guess or '-' in guess:		
			print "You can't get lucky if you're not listening."
			continue
		else:
			try:
				guess = int(guess)
			except:
				print "You can't get lucky if you're not listening."
				continue
			else:
				return guess


def test_guess(guess, digits):
	'''Function calls the function to generate a random number, 
	and compares it to the guess the user input. 

	If the guess is correct, the user is congratulated and the 
	program terminated. Otherwise, the user is given a hint as 
	to whether their guess was too low/high, and then prompted 
	to guess again.
	'''
	number = generate_random_number(digits)

	while guess != number:
		if guess > number:
			print "Your guess is a tad high. Try again!"
		else:
			print "Your guess is a tad low. Try again!"
		guess = user_guesses(digits)

	print "Congratulations, you're spot on!"
	return 

################################################################################

def main():
	'''Function generates a positive random integer and prompts the user to
	guess the correct number. After each guess, the computer will provide
	feedback to guide the user in making their next guess. 

	The number of digits for the random number may be given as an arg 
	when the function is called from the command line. 
	Otherwise, it defaults to a 1-digit number.
	'''
	digits = determine_digits()
	test_guess(user_guesses(digits), digits)  	#Is it better to have these in main, or in test_guess()? 
												#(see mimsmind2.py where I've moved them into test_guess().


if __name__ == "__main__":
	main()