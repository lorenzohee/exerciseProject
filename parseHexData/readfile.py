import codecs
class FilePluse:
	def __init__(self):
		self.filepath = '84218386.bin'
		self.pluseData = []
		self.hexData = []

	def readFile(self):
		with codecs.open(self.filepath, 'rt', encoding='utf-8', errors='ignore') as f:
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