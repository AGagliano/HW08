#!/usr/bin/env python
# Exercise 3  
# Dictionaries have a method called keys that returns the keys of the 
# dictionary, in no particular order, as a list.

# (1) Modify print_hist_old to print the keys and their values in alphabetical 
# order.

# (2) Paste in your completed functions from HW08_ex_11_02.py

# (3) Within main() make the appropriate function calls to print the
# alphabetical histogram of pledge.txt
##############################################################################

from string import ascii_letters

def print_hist_new(h):
    for key in sorted(h.keys()):
    	print key, h[key]

##############################################################################
################### INSERT COMPLETED CODE FROM 11_02 BELOW: ##################
##############################################################################

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
##############################################################################
def main():
    """ Calls print_hist_new with the appropriate arguments to print the 
    histogram of pledge.txt.
    """
    print_hist_new(histogram_new(get_pledge_list()))

if __name__ == '__main__':
    main()
