import nltk
import datareader
import wordsmith
import json

entries = nltk.corpus.cmudict.entries()
dictionary = dict(entries)

bucket = wordsmith.bucket

wordlist = dictionary.keys()
wordlist.extend(datareader.collocationEntries())

def seed():
	count = 0
	for w in wordlist:
		bucket.add(w)

		count+=1

		if count % 13000 == 0:
			print str((count/13000)*10) + " percent done loading"

	f = open('./nltk_data/bucketstore', 'a')
	f.write(json.dumps(bucket.buckets))