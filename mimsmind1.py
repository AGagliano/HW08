#!/usr/bin/env python

################################################################################

#Imports
import random
import sys

#Body
def determine_digits():
	'''Retrieves the number of digits from an arg given in the command line.
	If an arg is not given, the number of digits defaults to 3.

	Function returns the number of digits.
	'''
	try:
		digits = int(sys.argv[1])			
	except:
		digits = 3
		
	#Convert digit to default of 3, if user input is not applicable.
	if type(digits) is str or digits <=0:
		digits = 3

	return digits

def max_guesses(digits):
	'''Function calculates the maximum number of guesses the 
	user has in the game. The maximum number is a function
	of the number of digits.
	'''
	maxguesses = (2**digits) + digits
	return maxguesses

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
	#Guesses without the correct number of digits, 
	#negative guesses, decimals, and words are all 
	#inappropriate guesses.
	while True:
		guess = raw_input('Guess a positive integer with {0} digit{1}.\n>'.format(digits, digits_plural))
		if len(guess) != digits or '.' in guess or '-' in guess:		
			print "You can't get lucky if you're not listening."
			continue
		else:
			try:
				int(guess)
			except:
				print "You can't get lucky if you're not listening."
				continue
			else:
				return guess


def test_guess():
	'''Function calls other functions to generate the number of digits,
	the random number, and the maximum number of guesses.
	Function then compares the random number to the guess 
	the user input. 

	If the guess is correct, the user is congratulated and the 
	program terminated. Otherwise, the user is given a hint as 
	to whether their guess was too low/high, and then prompted 
	to guess again.

	The game terminates if the maximum number of guesses is reached.
	'''
	digits = determine_digits()
	number = str(generate_random_number(digits))
	maxguesses = max_guesses(digits)

	print 'Welcome to the mimsmind game. You have {0} tries to guess the random number.'.format(maxguesses)

	guess = user_guesses(digits)
	guess_str = str(guess)					
	guess_dict = {i:guess_str[i] for i, value in enumerate(guess_str)}	#I wanted to user enumerate here but couldn't figure out how.

	guess_count = 1

	while guess != number and guess_count < maxguesses:
		bulls = 0
		cows = 0
		number_used_list = [d for d in number]
		for digit in guess_dict:
			if guess_dict[digit] == number_used_list[digit]:
				bulls += 1
				number_used_list[digit] = 'used'
		for digit in guess_dict:
			if guess_dict[digit] in number_used_list:
				cows += 1
		print "{0} bull(s), {1} cow(s).".format(bulls, cows)
		guess = user_guesses(digits)
		guess_str = str(guess)								
		guess_dict = {i:guess_str[i] for i , value in enumerate(guess_str)}	#I wanted to user enumerate here but couldn't figure out how.
		guess_count += 1

	if guess == number:
		print "Congratulations, you're spot on!. You guessed the correct number in {0} tries.".format(guess_count)
	else:
		print "Sorry, but you've guessed {0} times. That is too many!".format(guess_count)
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
	test_guess()  


if __name__ == "__main__":
	main()