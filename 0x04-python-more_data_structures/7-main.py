#!/usr/bin/python3
from 7-update_dictionary import update_dictionary
from 6-print_sorted_dictionary import print_sorted_dictionary

a_dictionary = {'language': "C", 'number': 89, 'track': "Low level"}

new_dict = update_dictionary(a_dictionary, 'language', "Python")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)

print("--")
print("--")

new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)
