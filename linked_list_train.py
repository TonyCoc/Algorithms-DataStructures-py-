class Node():

	def __init__(self, data=None, Next=None):

		self.data = data

		self.next = Next
 

class LinkedList():

	def __init__(self):

		self.head = None


	def insert_at_begining(self, data):

		#pushing pervios first item to next index
		node = Node(data ,self.head)

		#replacing head item
		self.head = node


	def insert_at_end(self, data):

		if self.head is None:

			self.insert_at_begining(data)

			return None

		itr = self.head

		while itr.next:
			itr = itr.next

		itr.next = Node(data, None) 


	def insert_values(self, data_list):


		if self.head is None:

			i = data_list[0]

			self.insert_at_begining(i)

			

		itr = self.head

		for i in data_list:

			if i == itr.data:
				continue

			if itr.next is None:

				itr.next = Node(i,None)	


			itr = itr.next


	def get_length(self):

		if self.head is None:
			raise ValueError("empty list")

		else:

			counter = 1

			itr = self.head

			while itr.next:
				
				if itr.data is None:
		
					itr = itr.next
				else:
					counter += 1
					itr = itr.next
			

			return counter


	def print(self):

		if self.head is None:

			print("list is empty")

		itr = self.head
		li = ''

		while itr:

			if itr.data is None:
				itr = itr.next
			else:
				li += str(itr.data) + " ---> "
				itr = itr.next
			

		print(li)


	def remove_at(self, index):

		if index < 0 or index > self.get_length()-1:
			raise ValueError("Invalid index!!!")
		
		counter = 0

		itr = self.head

		#check if list is empty
		if itr is not None:
			while itr:
				if counter == index:
					if itr.next is None:
						itr.data = None
					else:
						while itr.next:
							itr.data = itr.next.data
							itr = itr.next
							break
						itr.data = None
						break
				counter += 1
				itr = itr.next
		else:
			raise ValueError("list is empty!!!")




	def insert_at(self, index, data):

		if index < 0 or index > self.get_length()-1:
			raise ValueError("Invalid index")

		counter = 0

		itr = self.head

		if index == 0:
			self.insert_at_begining(data)
		#check if list is empty
		if itr is not None:
			while itr:
				if counter == index-1:
					node = Node(data,itr.next)
					itr.next = node
				counter += 1
				itr = itr.next
		else:
			raise ValueError("list is empty!!!")


	def index_finder(self, expecting_value):

		index = 0     		

		is_Found = False 

		itr = self.head

		while itr: 				#identifing given value index

			if itr.data == expecting_value:

				is_Found = True 	#if given value exists in List
				break

			index += 1
			itr = itr.next

		if is_Found is False:
			raise ValueError("expecting value is not exists the list!!!")
		else:
			return index
	#exercise 1
	def insert_after_value(self, expecting_value, data ):

		index = self.index_finder(expecting_value)

		#like insert_at but with litle diffrent in "if counter == index:" line
		counter = 0

		itr = self.head

		if index == 0:
			self.insert_at_begining(data)
		#check if list is empty
		if itr is not None:
			while itr:
				if counter == index:
					node = Node(data,itr.next)
					itr.next = node
				counter += 1
				itr = itr.next
		else:
			raise ValueError("list is empty!!!")


	#exercise 2
	def remove_by_value(self, value):
		
		index = self.index_finder(value)

		if index < 0 or index > self.get_length()-1:
			raise ValueError("Invalid index!!!")
		
		counter = 0

		itr = self.head

		#check if list is empty
		if itr is not None:
			while itr:
				if counter == index:
					if itr.next is None:
						itr.data = None
					else:
						while itr.next:
							itr.data = itr.next.data
							itr = itr.next
							break
						itr.data = None
						break
				counter += 1
				itr = itr.next
		else:
			raise ValueError("list is empty!!!")




if __name__ == "__main__":
	ll = LinkedList()
	ll.insert_values([1,2,3,4,5])
	ll.remove_by_value(2)
	print(ll.get_length())
	ll.print()





