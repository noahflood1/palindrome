# © Noah Flood 2025
#
# Main runner file for this challenge.

from data import strings
from data import checker

# Noah's solution:
#from palindrome import is_palindrome

# your solution:
from my_solution import is_palindrome 

palindromes = []
negatives = []

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


