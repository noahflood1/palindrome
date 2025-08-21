# © Noah Flood 2025
#
# Check some different strings for multiple conditions, 
# utilizing short-circuiting for simpler conditions.

from solution.palindrome import is_palindrome

words = [
    "apple", "banana", "cat", "dog", "elephant", "fish", "grape", "house", "ice", "jungle",
    "kite", "lion", "monkey", "nest", "orange", "pencil", "queen", "rabbit", "sun", "tree",
    "umbrella", "violin", "water", "xylophone", "yacht", "zebra", "book", "chair", "desk", "egg",
    "flower", "garden", "hat", "island", "jacket", "kangaroo", "lamp", "mountain", "notebook", "ocean",
    "piano", "quilt", "river", "shoes", "table", "uniform", "village", "window", "xenon", "yogurt",
    "zoo", "ant", "ball", "cloud", "drum", "engine", "feather", "goat", "hill", "ink",
    "jewel", "key", "leaf", "mirror", "net", "owl", "pearl", "quill", "rose", "stone",
    "tiger", "urchin", "vase", "wheel", "axe", "yellow", "zip", "air", "bread", "coin",
    "doll", "ear", "fan", "gift", "hand", "iron", "jam", "king", "lamp", "moon",
    "nail", "oil", "pen", "queenly", "rope", "star", "train", "unit", "voice", "wing", "racecar"
	]

def cond1(word):
	return word[-1] == 's'
def cond2(word):
	return 'a' in word
def cond3(word):
	return word == 'elephant'			
def cond4(word):
	return is_palindrome(word)

print("words that fit your conditions:")

for word in words:
	if cond1(word) or cond2(word) or cond3(word) or cond4(word):
		print(word)
