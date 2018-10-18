class FilePluse:
	def __init__(self):
		self.filepath = 'test.txt'
		self.pluseData = []
		self.hexData = []

	def readFile(self):
		with open(self.filepath, 'rt') as f:
			for line in f:
				self.parseData(line)

	def parseData(self, data):
		lineArray = data.split( )
		self.pluseData = self.pluseData + lineArray[1:]

	def translateData(self):
		result = 0x0
		for tmp in self.pluseData:
			result = result + int(tmp, 16)
		print(hex(result))
		print(result)

if __name__ == "__main__":
	file = FilePluse()
	file.readFile()
	file.translateData()