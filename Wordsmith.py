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
from PhoneticBucket import PhoneticBucket

nltk.data.path.insert(0,'./nltk_data/')

entries = nltk.corpus.cmudict.entries()
dictionary = dict(entries)

pronDict = dict()
bucket = PhoneticBucket()

wordlist = dictionary.keys()

def setup():
	bucket.setBucket(DataReader.loadBucket())
	wordlist.extend(DataReader.collocationEntries())

	for w in wordlist:
		addStress(tokenize(w))

def addStress(pron):
	stress = []
	phonecount = 0
	for phone in pron:
		for char in phone:
			if char.isdigit():
				stress.append([int(char),phone, phonecount])
		phonecount = phonecount + 1

	pronDict[str(pron)] = stress

def getStress(pron):
	if not str(pron) in pronDict:
		addStress(pron)

	return pronDict[str(pron)]

def getPron(inputWord):
	if not inputWord in dictionary:
		return False

	inputPron = dictionary[inputWord]

	# if inputPron[-1] == 'NG' and len(getStress(inputPron)) > 1:
	# 	inputPron[-1] = 'N'

	return inputPron

def tokenize(word):
	pron = []

	wordsplit = word.split()
	for w in wordsplit:
		if (not w in dictionary):
			return []
		else:
			pron.extend(getPron(w))

	return pron

def getRelevantWords(word):
	return bucket.getListFromWord(word)