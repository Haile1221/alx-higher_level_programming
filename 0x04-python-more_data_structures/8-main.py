#!/usr/bin/python3
from 8-simple_delete import simple_delete
from 6-print_sorted_dictionary import print_sorted_dictionary

a_dictionary = {'language': "C", 'Number': 89, 'track': "Low", 'ids': [1, 2, 3]}

new_dict = simple_delete(a_dictionary.copy(), 'track')  # Use a copy to avoid modifying the original
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

print("--")
print("--")

new_dict = simple_delete(a_dictionary.copy(), 'c_is_fun')  # Use a copy to avoid modifying the original
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)
