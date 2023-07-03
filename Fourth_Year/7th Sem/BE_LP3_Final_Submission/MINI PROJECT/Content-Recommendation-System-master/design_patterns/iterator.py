class MyIterator:
	def __init__(self, c):
		self.c = c
		self.i = 0
	def __next__(self):
		#return "test"	
		if self.i < len(self.c) :
			self.i += 1
			return self.c[self.i - 1]
		else:
			raise StopIteration		

class MyCollection:
	def __init__(self, *args):
		self.c = args
	def __str__(self):
		return str(self.c)
	def __iter__(self):
		return MyIterator(self.c)
	
	
c1 = MyCollection(2,3,5,7,11)
c2 = MyCollection(1, 2, 4, 8, 16, 32)
print(c1)
print(c2)

it1 = iter(c1)
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
#print(next(it1))

print("first iteration")
for e in c1:
	print(e, end = " ")
print()
print("second iteration")
for e in c1:
	print(e, end = " ")
print()

it1 = iter(c1); it2 = iter(c1)
print(next(it1))
print(next(it2))








	
	
	
	
