# priority queue using heap
class PQ:

	def __init__(self):
		self.pq=[]
		self.lastPosition=0

	def add(self,element):
		self.pq.append(element)
		self.lastPosition=len(self.pq)-1
		self.trickleUp(self.lastPosition)

	def remove(self):
		if self.pq:
			elementValue=self.pq[0]
			self.swap(0,self.lastPosition)
			self.pq.pop()
			self.lastPosition=len(self.pq)-1
			self.trickleDown(0)
			return elementValue

	def trickleUp(self,position):
		if position == 0:
			return
		else:
			parent=(position-1)/2
			if self.pq[parent]<self.pq[position]:
				self.swap(parent,position)
				self.trickleUp(parent)


	def trickleDown(self,position):
		leftChild = 2*position+1
		rightChild=2*position+2
		if leftChild==self.lastPosition:
			if self.pq[leftChild]>self.pq[position]:
				self.swap(leftChild,position)
			return
		if rightChild==self.lastPosition:
			if self.pq[rightChild]>self.pq[position]:
				self.swap(rightChild,position)
			return
		if leftChild>self.lastPosition or rightChild > self.lastPosition:
			return

		if self.pq[leftChild]>self.pq[rightChild] and self.pq[leftChild]>self.pq[position]:
			self.swap(leftChild,position)
			self.trickleDown(leftChild)
		elif self.pq[rightChild]>self.pq[position]:
			self.swap(rightChild,position)
			self.trickleDown(rightChild)

	def swap(self,firstPosition,secondPosition):
		temp=self.pq[firstPosition]
		self.pq[firstPosition]=self.pq[secondPosition]
		self.pq[secondPosition]= temp

	def getLastPosition(self):
		return self.lastPosition


if __name__=="__main__":
	pq=PQ()
	pq.add(5)
	pq.add(9)
	pq.add(11)
	pq.add(10)
	pq.add(8)
	print pq.pq

	for i in range(len(pq.pq)):
		print pq.remove()


# 0
# 1 if on this parent pos-1/2 0
# 2
# 3
# 4
# stoping conditions 
# 1. if left  is last position then compare swap stop
# 2. if right is last postion then compare  
# 3. if left or right is greater than last position 
# 4. now in this condition both left and right child we will get to compare and swap with who is the daddy
