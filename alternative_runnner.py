from palindrome import is_palindrome_v2
from data import strings
from data import checker

pals = ""
for string in strings:
   if is_palindrome_v2(string):
      pals+=string
print("Checker: ", checker)
print("Pals: ", pals)
print(f"Success?: {pals == checker}")