#pylint:disable=C0116
#pylint:disable=C0115
#pylint:disable=C0103
# Here, we define the node classes
class LeafNode:
	def __init__(self, character, weight):
		self.character = character
		self.weight = weight
		self.boolParent = False
		
	def getWeight(self):
		return self.weight
			
	def getChar(self):
		return self.character
		
	def setParent(self):
		self.boolParent = True
		
	def getParent(self):
		return self.boolParent
	
		
class BranchNode:
	def __init__(self, left, right):
		self.leftNode = left
		self.rightNode = right
		self.boolParent = False
	
	def getWeight(self):
		return self.leftNode.getWeight() + self.rightNode.getWeight()
	
	def setParent(self):
		self.boolParent = True
		
	def getParent(self):
		return self.boolParent
		
	def getLeftNode(self):
		return self.leftNode
		
	def getRightNode(self):
		return self.rightNode


# This snippet counts the amount of characters,
# and gives us a dictionary with the amount of characters.
with open("testfile.txt", "r") as f:
	line = f.readline()
	charset = {}
	for char in line:
		if char in charset.keys():
			charset[char] +=1
		else:
			charset[char] = 1

# Here, we put all characters and their associated weights into LeafNodes.
leafNodeList = []
for key in charset.keys():
	leafNodeList.append(LeafNode(key, charset[key]))
	
# Here, we get the highest number that a character occurs.
highest = leafNodeList[0]
for node in leafNodeList:
	if node.getWeight() > highest.getWeight():
		highest = node

branchNodeList = []
# Here, we set our current lowest occurrence to the highest number,
# because we decrease that as we iterate through the list,
# and this is currently our only known value.

# Here, the main tree generation loop starts.
 
combinedNodeList = leafNodeList + branchNodeList

lowest = highest
secondLowest = lowest

print(lowest.getChar())

for node in combinedNodeList:
	if not node.getParent():
		print(node.getChar(), node.getWeight())
		if node.getWeight() <= lowest.getWeight() or lowest.getParent() or secondLowest.getParent():
			secondLowest = lowest
			lowest = node
			
branchNodeList.append(BranchNode(lowest, secondLowest))
lowest.setParent()
secondLowest.setParent()

for node in branchNodeList:
	print(node.leftNode.getChar())
	print(node.rightNode.getChar())
