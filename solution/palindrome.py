# © Noah Flood 2025
# Checks whether or not a given string is a palindrome, returning a boolean indicator.
#
# I had a dream last night that someone asked me how to check some strings for different conditions
# and in the dream, I couldn't remember how. It reminded me of this coding problem and made me want to re-approach it
# from scratch without outside help.
#
# The only AI used for this project was to lookup low-level Python syntax, and to get a list of test strings.
# This was my real solution to the problem, in Python.

import math

#
# My goal was to iterate over the front and back of the target string simultaneously,
# comparing the results as we go, stopping when there is a mismatch, or when enough characters have been evaluated.
#
def is_palindrome(word):
	front = ""
	back = ""
	i = 0
	while i < len(word): # at this level, we will iterate over the whole string
		front+=word[i]
		back+=word[-i - 1] # need this indexing because in python, you can only index the last letter of the word with -1, not -0
		if not (front == back): # short circuit if theres a mismatch to save time
			print(f"Breaking because {front} is not equal to {back}.\n")
			return False
		print(f"{front} == {back}")
		i += 1
		if i >= math.ceil(len(word) / 2): # if we're past halfway, we don't have to check anymore. could put this into the top level loop but wanted to explicitly check this
			print(f"Breaking because index {i} is past half-way, so {word} must be a palindrome!\n")
			return True 
	return True

# an alternative/refactor i came up with after completing the above
def is_palindrome_v2(string):
	i = 0
	while i < math.ceil(len(string) / 2):
		if not (string[i] == string[-i - 1]):
			return False
		i+=1
	return True

# TODO: out of curiosity, see what funcitons exist in javascript to implement this
