import nltk
import DataReader
import Wordsmith
import json

entries = nltk.corpus.cmudict.entries()
dictionary = dict(entries)

bucket = Wordsmith.bucket

wordlist = dictionary.keys()
wordlist.extend(DataReader.collocationEntries())

def seed():
	count = 0
	for w in wordlist:
		bucket.add(w)

		count+=1

		if count % 20000 == 0:
			print str((count/20000)*10) + " percent done loading"

	f = open('./nltk_data/bucketstore', 'a')
	f.write(json.dumps(bucket.buckets))