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

def getBinary(previousPath, curRootNode, binaryCodeSet):
	leftNode = curRootNode.getLeftNode()
	if type(leftNode) is LeafNode:
		print('{}: {}'.format(leftNode.getChar(), previousPath + '0'))
		binaryCodeSet[leftNode.getChar()] = previousPath + '0'
	else:
		binaryCodeSet = getBinary(previousPath + '0', leftNode, binaryCodeSet)
	
	rightNode = curRootNode.getRightNode()
	if type(rightNode) is LeafNode:
		print('{}: {}'.format(rightNode.getChar(), previousPath + '1'))
		binaryCodeSet[rightNode.getChar()] = previousPath + '1'
	else:
		getBinary(previousPath + '1', rightNode, binaryCodeSet)
		binaryCodeSet = getBinary(previousPath + '1', rightNode, binaryCodeSet)
	return binaryCodeSet


# This snippet counts the amount of characters,
# and gives us a dictionary with the amount of characters.
with open('testfile.txt', 'r') as f:
	charset = {}
	for char in f.read():
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
	print('"{0}": {1}'.format(node.getChar(), node.getWeight()))
	if node.getWeight() > highest.getWeight():
		highest = node

branchNodeList = []

# Here, the main tree generation loop starts.
while sum([node.getParent() is False for node in leafNodeList]) != 0 or sum([node.getParent() is False for node in branchNodeList]) != 1:
	
	print('==============================')
	print('leafNodeList: {}'.format(sum([node.getParent() is False for node in leafNodeList])))
	print('branchNodeList: {}'.format(sum([node.getParent() is False for node in branchNodeList])))
	
	combinedNodeList = leafNodeList + branchNodeList
	
	print('len(branchNodeList): {}'.format(len(branchNodeList)))
	
	# Here, we set our current lowest occurrence to the highest number,
	# because we decrease that as we iterate through the list,
	# and this is currently our only known value.
	lowest = highest
	secondLowest = lowest
	
	for node in combinedNodeList:
		if not node.getParent():
			if node.getWeight() <= lowest.getWeight() or lowest.getParent() or secondLowest.getParent():
				secondLowest = lowest
				lowest = node
				
	branchNodeList.append(BranchNode(lowest, secondLowest))
	lowest.setParent()
	secondLowest.setParent()
	
rootNode = list(filter(lambda c: c.getParent() is False, branchNodeList))[0]

print(rootNode)

# I need some recursive function that first explores the left side of the tree,
# and then explores the right side. I definitely need some way to store the current position
# in the binary tree to be able to print the binary value of the leaf node.
# The previous path is passed to the function as an argument

binaryCode = getBinary('', rootNode, {})

print(binaryCode)

with open('testfile.txt', 'r') as f:
	outstring = ''
	with open('outfile.txt', 'w') as o:
		for char in f.read():
			outstring += binaryCode[char]
		o.write(outstring)
			