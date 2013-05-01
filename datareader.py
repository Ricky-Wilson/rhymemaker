def collocationEntries():
	f = open('./nltk_data/collocations', 'r')

	entries = []
	for line in f:
		entries.append(line[:-1])

	g = open('./nltk_data/collocations3', 'r')
	for line in g:
		entries.append(line[:-1])

	return entries