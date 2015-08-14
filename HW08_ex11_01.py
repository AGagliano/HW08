#!/usr/bin/env python
# Exercise 1  
# Write a function that reads the words in words.txt and stores them as keys
# in a dictionary (returning the dictionary). It doesnt matter what the 
# values are. Then you can use the in operator as a fast way to check whether
# a string is in the dictionary.
##############################################################################

def store_to_dict():
    '''Function reads words.txt and stores the words as keys in a dictionary, 
    and returns the dictionary. 

    The corresponding values are the lengths of the keys.
    '''
    with open('words.txt') as f:
    	l = f.readlines()
    	d = {word.strip():len(word) for word in l}
    return d


##############################################################################
def main():  # DO NOT CHANGE BELOW
    words_dict = store_to_dict()
    if "this" in words_dict:
        print "Yup."
    if "qwertyuiop" in words_dict:
        print "Hmm."

if __name__ == '__main__':
    main()
