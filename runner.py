# © Noah Flood 2025
#
# Main runner file for this challenge.

import time
import argparse # for parsing commandline arguments
import tools
from data import string_pool

# --- import the palindrome checker functions ----

# wire up solutions
from solution.palindrome import is_palindrome as solution1
from solution.palindrome import is_palindrome_v2 as solution2
from my_solution import is_palindrome as my_solution

# --- handle commandline arguments ----

parser = argparse.ArgumentParser(description="for setting solution options and number of strings to process")

# add required commandline arguments
parser.add_argument("-m", "--method", choices=["solution1, solution2, my_solution"], required=True, help="Which solution to use")
parser.add_argument("-n", type="int", default=100, help="Number of strings to process")
# action=("store_true") makes it a boolean flag where if it shows up, it is true, and if not, it is false
parser.add_argument("-v", "--silent", action="store_true", help="Enable verbose mode") 

# this actually parses the command-line arguments
args = parser.parse_args()

# --- get a new, semi-unique set of strings to test ----

# get a list of test strings which is n long
# where n is the number of strings the user specified
test_strings = tools.get_data(strings=string_pool, n=args.n)

# should return a string that includes all of the correctly parsed strings from the input
#FIXME: make it more complex than just a solution so you can get better feedback
solution_string = tools.get_solution(data=test_strings)

# --- get the solution for this set ----
# the solution will be a two dimenensional array [3xn] that stores the word being tested, the 




















for string in strings:
	print(f"CHECKING \"{string}\"...")
	print(f"##############" + "#" * len(string))
	if is_palindrome(string):
		palindromes.append(string)
	else:
		negatives.append(string)

test_string = ""
for i in palindromes:
	test_string += i

print("\n###########")
print("# RESULTS #")
print("###########")

print(f"{len(palindromes)} strings were marked as palindromes.")
print(f"{len(negatives)} strings were marked as non-palindromes.")

if test_string == checker:
	print("\n***You successfully found all palindromes in the list!***")
else:
	print("\nYour code has errors, but this is where the learning happens. Try again!")


