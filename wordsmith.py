import nltk

nltk.data.path.append('./nltk_data/')

entries = nltk.corpus.cmudict.entries()
dictionary = dict(entries)

def getStress(pron):
	stress = []
	phonecount = 0
	for phone in pron:
		for char in phone:
			if char.isdigit():
				stress.append([int(char),phone, phonecount])
		phonecount = phonecount + 1

	return stress

def getPron(inputWord):
	if not inputWord in dictionary:
		return False

	inputPron = dictionary[inputWord]

	if inputPron[-1] == 'NG' and len(getStress(inputPron)) > 1:
		inputPron[-1] = 'N'

	return inputPron