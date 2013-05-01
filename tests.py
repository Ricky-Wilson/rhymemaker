import rhymemaker
import time
import wordsmith

def timed(str):
	t0 = time.time()
	results = rhymemaker.rhyme(str)
	t1 = time.time()

	print results
	return t1-t0
