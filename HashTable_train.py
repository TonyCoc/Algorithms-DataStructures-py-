class HashTable:

	def __init__(self):
		
		self.array_size = 100

		self.array = [[] for _ in range(100)]


	def get_hash(self, key):

		total = 0

		for char in key:

			total += ord(char)

		return total % self.array_size

	def __getitem__(self, key):

		index = self.get_hash(key)

		if len(self.array[index]) >= 1:
			for i in self.array[index]:
				if i[0] == key:
					return i[1]
		
		

	def __setitem__(self, key, value):

		index = self.get_hash(key)

		dup_set = False

		if len(self.array[index]) >= 1:

			for i in self.array[index]:
				if i[0] == key:
					i[1] = value
					dup_set = True
					break
				else:
					pass

			if not dup_set:
				self.array[index].append([key, value])
				
			
		else:
			self.array[index].append([key, value])


h = HashTable()
h["22"] = 'sss' 
h['d'] = 'ss'
