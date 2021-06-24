import json

# Here, we load the binary dict from our file and parse it into a dictionary with the help of json.loads().
with open('binarytreefile.txt', 'r') as f:
	binaryCodeUninverted = json.loads(f.read())

# Here, we invert the dictionary so the characters, which were previously keys, now become values,
# and the previous values now become keys.
binaryCode = {}
for key in binaryCodeUninverted:
	binaryCode[binaryCodeUninverted[key]] = key
	
print(binaryCode)

# We read the binary file completely and store it in a var.
with open('outfilebinary.txt', 'r') as f:
	content = f.read()

# We read the binary text bit for bit, and continue appending our binaryWord variable until
# it matches a key in the dictionary.
binaryWord = ''
decodedText = ''
for character in content:
	binaryWord += character
	if binaryWord in binaryCode.keys():
		decodedText += binaryCode[binaryWord]
		binaryWord = ''

# We then write our decoded text into another file.
with open('outfiletext.txt', 'w') as f:
	f.write(decodedText)


