import Wordsmith

class PhoneticBucket:
	def __init__(self):
		self.buckets = dict()

	def add(self, word):
		stress = Wordsmith.getStress(Wordsmith.tokenize(word))
		if (len(stress) < 1):
			return False
		phone = stress[-1][1]
		if phone not in self.buckets.keys():
			self.buckets[phone] = []
		if not word in self.buckets[phone]:
			self.buckets[phone].append(word)

	def get(self, phone):
		if phone not in self.buckets.keys():
			return None
		return self.buckets[phone]

	def setBucket(self, bucket):
		self.buckets = bucket

	def getListFromWord(self,word):
		stress = Wordsmith.getStress(Wordsmith.tokenize(word))
		if (len(stress) < 1):
			return False
		phone = stress[-1][1]
		return self.get(phone)





