def collocationEntries():
	f = open('./nltk_data/collocations', 'r')

	entries = []
	for line in f:
		entries.append(line[:-1])

	return entries