#!/usr/bin/env python
# Exercise 4  
# (1) Modify reverse_lookup_old so that it builds and returns a list of all
# keys that map to v, or an empty list if there are none.

# (2) Paste in your completed functions from HW08_ex_11_02.py

# (3) Do not edit what is in main(). It should print what is returned, a list
# of the keys that map to the values passed.
##############################################################################

def reverse_lookup_new(d, v):
    l = [key for key in d if d[key] == v]
    return l

##############################################################################
################### INSERT COMPLETED CODE FROM 11_02 BELOW: ##################
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
################### INSERT COMPLETED CODE FROM 11_02 ABOVE: ##################
##############################################################################
def main():   # DO NOT CHANGE BELOW	
    pledge_histogram = histogram_new(get_pledge_list())
    print reverse_lookup_new(pledge_histogram, 1)
    print reverse_lookup_new(pledge_histogram, 9)
    print reverse_lookup_new(pledge_histogram, "Python")

if __name__ == '__main__':
    main()
