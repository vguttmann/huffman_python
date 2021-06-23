import json

with open('binarytreefile.txt', 'r') as f:
	binaryCodeUninverted = json.loads(f.read())
	
binaryCode = {}
for key in binaryCodeUninverted.keys():
	binaryCode[binaryCodeUninverted[key]] = key
	
print(binaryCode)
	
with open('outfilebinary.txt', 'r') as f:
	content = f.read()

binaryWord = ''
decodedText = ''
for character in content:
	binaryWord += character
	if binaryWord in binaryCode.keys():
		decodedText += binaryCode[binaryWord]
		binaryWord = ''
		
with open('outfiletext.txt', 'w') as f:
	f.write(decodedText)


