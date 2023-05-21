def binary_search(li,sub):
	li.sort()

	mid = int(round(len(li) / 2.0,0))

	li = li

	while li:
		print(li)
		print(mid)
		try:
			if len(li) <= 3:
					for i in li:
						if sub == i:
							print("Found!!!")
							li = None
							break
						else:
							pass
			if sub > li[mid]:
				
				li = li[mid:]
				mid = int(round(len(li) / 2.0 ,0))
				
				
			if sub < li[mid]:
			
				li = li[:mid]
				mid = int(round(len(li) / 2.0 ,0))

		except :
			break


		


binary_search(li=[1,2,3,4,5,6,7,8,9,10,11,12,13,14],sub=2)

my_l = []
my_l.sort