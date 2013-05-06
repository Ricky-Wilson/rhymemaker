# The MIT License (MIT)

# Copyright (c) 2013 Yat Choi

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

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