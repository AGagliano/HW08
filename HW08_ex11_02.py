#!/usr/bin/env python
# Exercise 2  
# Dictionaries have a method called get that takes a key and a default value.
# If the key appears in the dictionary, get returns the corresponding value; 
# otherwise it returns the default value. For example:

# >>> h = histogram('a')
# >>> print h
# {'a': 1}
# >>> h.get('a', 0)
# 1
# >>> h.get('b', 0)
# 0

# (1) Use get to write histogram_old more concisely. You should be able to
# eliminate the if statement.

# (2) Use histogram_new to take pledge.txt and create a dict histogram with
# word counts (do not change the case of the words).
##############################################################################

# Imports
from string import ascii_letters

# Body
def histogram_old(s):
    d = dict()
    #For each letter in the string s, if the letter exists as a key, 
    #increase the value by 1. If the letter doesn't exist as a key, 
    #add the key to the dictionary and assign it a value 1.
    for c in s:
        d[c] = d.get(c, 0) + 1  
    return d

def histogram_new(l):
    '''Counts the instances of a word in a list and returns a dictionary
    of word counts for each word.
    '''
    d = dict()
    for word in l:
        d[word] = d.get(word, 0) + 1
    return d


def get_pledge_list():
    """ Opens pledge.txt and converts to a list, each item is a word in 
    the order it appears in the original file. returns the list.
    """
    with open('pledge.txt') as f:
        pledge_list = f.read().split()

        #Eliminate punctuation from the end of words
        pledge_list_noPunct = [word if word[-1] in ascii_letters else word[:-1] for word in pledge_list]

    return pledge_list_noPunct


##############################################################################
def main():  # DO NOT CHANGE BELOW
    print histogram_new(get_pledge_list())

if __name__ == '__main__':
    main()
