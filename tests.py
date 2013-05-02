import RhymeMaker
import time
import Wordsmith

def timed(str):
	t0 = time.time()
	results = RhymeMaker.rhyme(str)
	t1 = time.time()

	print results
	return t1-t0
