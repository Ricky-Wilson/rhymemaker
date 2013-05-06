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





