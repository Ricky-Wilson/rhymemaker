import wordsmith

def nearSyllableScore(syllable1, syllable2):
	if (syllable1[0] == syllable2[0]) and (syllable1[1] == syllable2[1]):
		return 1
	elif (syllable1[0] != 1 and syllable2[0] != 1):
		if ((syllable1[1][:2] == 'IH' and syllable2[1][:2] == 'AH') or (syllable1[1][:2] == 'AH' and syllable2[1][:2] == 'IH')):
			return 0.5

	return -1

def nearConsonantScore(cons1, cons2):
	if (cons1 == cons2):
		return 1
	else:
		return 0

def rhyme(word, maxnum):
	rhymes = getNearRhymes(word)

	output = []

	count = 0
	for i in range(len(rhymes)):
		output.append(rhymes[i][0])
		count += 1
		if count == maxnum:
			break

	return output

def getNearRhymes(inWord):
	rhymes = []
	if (not inWord in wordsmith.dictionary):
		return []

	for word in wordsmith.dictionary.keys():
		score = nearRhymeScore(word, inWord)
		if score > 0:
			rhymes.append((word, score))

	
	return sorted(rhymes, key=lambda t: t[1], reverse=True)

def nearRhymeScore(word1, word2):
	if word1 == word2:
		return -1

	pron1 = wordsmith.getPron(word1)
	pron2 = wordsmith.getPron(word2)

	if not pron1:
		print ("Could not recognize " + word1)
		return -1

	if not pron2:
		print ("Could not recognize " + word2)
		return -1

	stress1 = wordsmith.getStress(pron1)
	stress2 = wordsmith.getStress(pron2)

	if not stress1 or not stress2:
		return -1

	if (nearSyllableScore(stress1[-1], stress2[-1]) < 0):
		# print ("Last syllable not similar enough")
		return -1

	match = 0

	if (len(stress1) > len(stress2)):
		tempStress = stress1
		stress1 = stress2
		stress2 = tempStress

		tempPron = pron1
		pron1 = pron2
		pron2 = tempPron

	for i in range(1,len(stress1)+1):
		# Check same stress pattern of word
		if (stress1[-i][0] != stress2[-i][0]):
			# print("Syllable stressing is different on syllable #%s" % -i)
			match = -1
			break
		# Check that important stresses rhyme
		elif ((stress1[-i][0] > 0) and (stress1[-i][1] != stress2[-i][1])):
			# print("Important Syllable %s does not rhyme" % -i)
			match = -1
			break
		# Check surrounding consonants for closeness
		else:
			match += nearSyllableScore(stress1[-i], stress2[-i])
			if (stress1[-i][2] > 0) and (stress2[-i][2] > 0) and (stress1[-i][2] < len(pron1) - 1) and (stress2[-i][2] < len(pron2)-1):
				index1 = stress1[-i][2]
				index2 = stress2[-i][2]

				match += nearConsonantScore(pron1[index1+1], pron2[index2+1])

	return match




