import nltk

entries = nltk.corpus.cmudict.entries()

def getStress(pron):
	stress = []
	for phone in pron:
		for char in phone:
			if char.isdigit():
				stress.append([int(char),phone])

	return stress

def getPron(inputWord):
	inputPron = []

	for word,pron in entries:
	 if word==inputWord:
	 	inputPron = pron

	return inputPron

def getNearRhymes(inWord):
	inPron = getPron(inWord)
	inStress = getStress(inPron)
	stressSize = len(inStress)
	rhymes = []
	for word, pron in entries:
		stress = getStress(pron)
		if (inWord == word):
			continue
		if len(stress) != stressSize:
			continue
		if (stress[-1][1] != inStress[-1][1]):
			continue

		for i in range(len(stress)):
			if ((inStress[i][0] > 0) and (stress[i][1] == inStress[i][1])):
				rhymes.append(word)


	return rhymes



