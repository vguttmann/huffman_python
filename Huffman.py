'This disables pylint warnings for not using snake_case.'
#pylint:disable=C0103

# Here, we import the JSON library to export the binary dictionary later on.
import json


# Here, we define the two node classes.

class LeafNode:
	'This is our LeafNode class which stores a character and its associated weight.'
	def __init__(self, character, weight):
		self.character = character
		self.weight = weight
		self.boolParent = False

	def getWeight(self):
		'getWeight() returns the weight of the associated character.'
		return self.weight

	def getChar(self):
		'getChar() returns the character of this node.'
		return self.character

	def setParent(self):
		'setParent() sets this node to have an associated parent node.'
		self.boolParent = True

	def getParent(self):
		'getParent() returns whether this node has a Parent or not.'
		return self.boolParent


class BranchNode:
	'This is our BranchNode class, which will link all the LeafNodes together.'
	def __init__(self, left, right):
		self.leftNode = left
		self.rightNode = right
		self.boolParent = False

	def getWeight(self):
		'getWeight() returns the nodes overall weight of the node and its child nodes.'
		return self.leftNode.getWeight() + self.rightNode.getWeight()

	def setParent(self):
		'setParent() sets this node to have an associated parent node.'
		self.boolParent = True

	def getParent(self):
		'getParent() returns whether this node has a Parent or not.'
		return self.boolParent
		
	def getLeftNode(self):
		'getLeftNode() returns the left child node.'
		return self.leftNode
		
	def getRightNode(self):
		'getRightNode() returns the right child node.'
		return self.rightNode


def getBinary(previousPath, curRootNode, binaryCodeSet):
	'''This function explores the binary tree, and in this process extracts the binary values
for the different characters.
The print function for this is broken, but frankly, I can't be bothered debugging that.'''
	leftNode = curRootNode.getLeftNode()
	if isinstance(leftNode, LeafNode):
		print('{}: {}'.format(leftNode.getChar(), previousPath + '0'))
		binaryCodeSet[leftNode.getChar()] = previousPath + '0'
	else:
		binaryCodeSet = getBinary(previousPath + '0', leftNode, binaryCodeSet)
	
	rightNode = curRootNode.getRightNode()
	if isinstance(rightNode, LeafNode):
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
for key in charset:
	leafNodeList.append(LeafNode(key, charset[key]))

# Here, we get the highest number that a character occurs so we can use that as a strarting
# point for finding the lowest number of characters.
highest = leafNodeList[0]
for node in leafNodeList:
	print('"{0}": {1}'.format(node.getChar(), node.getWeight()))
	if node.getWeight() > highest.getWeight():
		highest = node

branchNodeList = []

# Here, the main tree generation loop starts.
# We loop through the tree generation until every node in LeafNodeList has a parent,
# and the number of BranchNodes without a parent is 1
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
				
# Adding a branched node to their list, and setting both leaf nodes to have parents
# so they won't be used in further binary tree construction
	branchNodeList.append(BranchNode(lowest, secondLowest))
	lowest.setParent()
	secondLowest.setParent()

# This filters for the node which doesn't have a parent, which obviously must be our root node.
rootNode = list(filter(lambda c: c.getParent() is False, branchNodeList))[0]

print(rootNode)

# I need some recursive function that first explores the left side of the tree,
# and then explores the right side. I definitely need some way to store the current position
# in the binary tree to be able to print the binary value of the leaf node.
# The previous path is passed to the function as an argument
print('////////////////////////////////')
binaryCode = getBinary('', rootNode, {})
print('////////////////////////////////')
print(binaryCode)
print('////////////////////////////////')

with open('testfile.txt', 'r') as f:
	outstring = ''
	with open('outfilebinary.txt', 'w') as o:
		for char in f.read():
			outstring += binaryCode[char]
		o.write(outstring)

# This bit of code writes our binary dictionary to a second file which makes decoding much easier.
with open('binarytreefile.txt', 'w') as f:
	f.write(json.dumps(binaryCode))
