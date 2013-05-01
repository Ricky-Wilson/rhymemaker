import nltk
import datareader
from PhoneticBucket import PhoneticBucket

nltk.data.path.insert(0,'./nltk_data/')

entries = nltk.corpus.cmudict.entries()
dictionary = dict(entries)

pronDict = dict()
bucket = PhoneticBucket()
bucket.setBucket(datareader.loadBucket())

wordlist = dictionary.keys()
wordlist.extend(datareader.collocationEntries())

def setup():
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