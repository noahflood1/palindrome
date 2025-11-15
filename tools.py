from solution.palindrome import is_palindrome_v2 as is_palindrome
import random
from typing import List, Sequence, Optional, Iterable

print("Completes")

# define a log() command that handles when the display functions are called or not
def log(silent_mode, txt=""):
	if not silent_mode:
		print(txt)

def get_data(n: int, strings: Sequence[str], seed: Optional[int] = None) -> List[str]:
	"""
	Return n items sampled from `strings` in random order, unique within each
	pass over the pool. If n > len(strings), it resamples by reshuffling and
	continuing, so duplicates only happen across passes.
	"""
	# by using seeded, we can test with the same subgroup each time
	
	# if the length is less than zero or the provided sequence is empty, go ahead and return an empty list
	if n <= 0 or not strings:
		return []

	rng = random.Random(seed)	
	out: List[str] = [] # type hint of what the output will contain

	def func(left)





