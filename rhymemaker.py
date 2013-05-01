import wordsmith

def nearSyllableScore(syllable1, syllable2):
	if ((syllable1[0] == syllable2[0]) and (syllable1[1] == syllable2[1])):
		return 2

	score = -1
	if (syllable1[1][:2] == syllable2[1][:2]):
		score = 1.8
	elif ((syllable1[1][:2] == 'IH' and syllable2[1][:2] == 'AH') or (syllable1[1][:2] == 'AH' and syllable2[1][:2] == 'IH')):
		score = 0.5
	elif ((syllable1[1][:2] == 'IH' and syllable2[1][:2] == 'IY') or (syllable1[1][:2] == 'IY' and syllable2[1][:2] == 'IH')):
		score = 0.3
	elif ((syllable1[1][:2] == 'AA' and syllable2[1][:2] == 'AO') or (syllable1[1][:2] == 'AO' and syllable2[1][:2] == 'AA')):
		score = 0.5
	elif ((syllable1[1][:2] == 'AH' and syllable2[1][:2] == 'AO') or (syllable1[1][:2] == 'AO' and syllable2[1][:2] == 'AH')):
		score = 0.5
	elif ((syllable1[1][:2] == 'AH' and syllable2[1][:2] == 'AY') or (syllable1[1][:2] == 'AY' and syllable2[1][:2] == 'AH')):
		score = 0.2
	elif ((syllable1[1][:2] == 'AY' and syllable2[1][:2] == 'AE') or (syllable1[1][:2] == 'AE' and syllable2[1][:2] == 'AY')):
		score = 0.5
	elif ((syllable1[1][:2] == 'AO' and syllable2[1][:2] == 'AE') or (syllable1[1][:2] == 'AE' and syllable2[1][:2] == 'AO')):
		score = 0.5
	elif ((syllable1[1][:2] == 'EY' and syllable2[1][:2] == 'AH') or (syllable1[1][:2] == 'AH' and syllable2[1][:2] == 'EY')):
		score = 0.25

	if (syllable1[0] == 1 and syllable2[0] == 1):
		score *= 0.25
	elif (syllable1[0] == 1 or syllable2[0] == 1):
		score *= 0.75
	elif(syllable1[0] != syllable2[0]):
		score *= 0.8

	return score

def nearConsonantScore(cons1, cons2):
	if (cons1 == cons2):
		return 1.2
	elif ((cons1 == 'T' and cons2 == 'D') or (cons1 == 'D' and cons2 == 'T')):
		return 1
	elif ((cons1 == 'S' and cons2 == 'Z') or (cons1 == 'Z' and cons2 == 'S')):
		return 1
	elif ((cons1 == 'S' and cons2 == 'T') or (cons1 == 'T' and cons2 == 'S')):
		return 0.4
	else:
		return 0

def rhyme(word, maxnum=50):
	rhymes = getNearRhymes(word)

	output = []

	count = 0
	for i in range(len(rhymes)):
		output.append(rhymes[i][0])
		count += 1
		if count == maxnum:
			break

	return output

def getNearRhymes(inputString):
	rhymes = []
	pron1 = tokenize(inputString)

	for word in wordsmith.dictionary.keys():
		if inputString == word:
			continue
		elif "'" in word:
			continue

		pron2 = tokenize(word)
		
		score = nearRhymeScore(pron1, pron2)
		if score > 0:
			rhymes.append((word, score))

	
	return sorted(rhymes, key=lambda t: t[1], reverse=True)

def nearRhymeScore(pron1, pron2):

	stress1 = wordsmith.getStress(pron1)
	stress2 = wordsmith.getStress(pron2)

	if not stress1 or not stress2:
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
		if (stress1[-i][0] == stress2[-i][0]):
			match+= 1

		score = nearSyllableScore(stress1[-i], stress2[-i])
		if (score < 0):
			match = -1
			break

		else:
			if (stress1[-i][2] > 0) and (stress2[-i][2] > 0) and (stress1[-i][2] < len(pron1) - 1) and (stress2[-i][2] < len(pron2)-1):
				index1 = stress1[-i][2]
				index2 = stress2[-i][2]

				# Check surrounding consonants for closeness
				consonantScore = nearConsonantScore(pron1[index1+1], pron2[index2+1])
				if i == 1:
					score *= 1.5
					if score > 1:
						consonantScore *= 2.5
				# if i == 2:
				# 	consonantScore *=1.5
				print stress1[-i]
				print stress2[-i]
				print score
				print consonantScore

				match+=score
				match+= consonantScore

	return match

def tokenize(word):
	pron = []

	wordsplit = word.split()
	for w in wordsplit:
		if (not w in wordsmith.dictionary):
			return []
		else:
			pron.extend(wordsmith.getPron(w))

	return pron

def check(inputString, word):
	if inputString == word:
		return -1

	pron1 = tokenize(inputString)
	pron2 = tokenize(word)

	print pron1
	print pron2
		
	return nearRhymeScore(pron1, pron2)


