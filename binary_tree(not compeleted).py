class Btn():

	def __init__(self,parent=None,child_R=None,child_L=None,data):

		self.parent = parent

		self.child_R = child_R

		self.child_L = child_L

		self.data = data


	def insert(self,data,root): 

		node = root		

		while node.child_L != None or node.child_R != None:
			if node.child_L is None:
			if data > node.data: 





