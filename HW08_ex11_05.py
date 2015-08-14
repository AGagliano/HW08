#!/usr/bin/env python
# Exercise 5
# (1) Write a more concise version of invert_dict_old.

# (2) Paste in your completed functions from HW08_ex_11_02.py

# (3) Update print_hist_new from HW08_ex_11_03.py to be able to print
# a sorted version of the dict (print key/value pairs from 0 through the
# largest key values, (and those in between))
# Ex. If d = {1:["this, that"], 3: ["the"]}, it prints:
#    '1: ["this", "that"]'
#    '2:'
#    '3: ["the"]'
##############################################################################

#Imports
from collections import defaultdict

#Body
def invert_dict_old(d):
    inverse = dict()
    for key in d:                               
        val = d[key]                        
        if val not in inverse:
            inverse[val] = [key]            
        else:
            inverse[val].append(key)
    return inverse


def invert_dict_new(d):
    inverse = defaultdict(list)
    for key, value in d.items():
        inverse[value].append(key)
    return inverse

def print_hist_newest(d):
    max(d.keys())
    for key in range(0,max(d.keys())+1):
        print key, d[key]

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
def main():  # DO NOT CHANGE BELOW

    pledge_histogram = histogram_new(get_pledge_list())
    pledge_invert = invert_dict_new(pledge_histogram)
    print_hist_newest(pledge_invert)

if __name__ == '__main__':
    main()
