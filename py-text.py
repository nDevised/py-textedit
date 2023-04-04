import shlex

class ItemError(Exception):

	def __init__(self,msg=None):
		"""
		This exception is meant to be raised when an illegal file type (not .txt) is attempted to be loaded
		:param msg: A string of the message that may be entered (it is None by default, so nothing needs to be entered)
		"""
		self.msg = msg

class EmptyFileError(Exception):

	def __init__(self, msg=None):
		"""
		This exception is meant to be raised when an illegal file type (not .txt) is attempted to be loaded
		:param msg: A string of the message that may be entered (it is None by default, so nothing needs to be entered)
		"""
		self.msg = msg

class InvalidArgument(Exception):

	def __init__(self, msg=None):
		"""
		This exception is meant to be raised when an illegal file type (not .txt) is attempted to be loaded
		:param msg: A string of the message that may be entered (it is None by default, so nothing needs to be entered)
		"""
		self.msg = msg

class InvalidCommand(Exception):

	def __init__(self, msg=None):
		"""
		This exception is meant to be raised when an illegal file type (not .txt) is attempted to be loaded
		:param msg: A string of the message that may be entered (it is None by default, so nothing needs to be entered)
		"""
		self.msg = msg

class IllegalLine(Exception):

	def __init__(self, msg=None):
		"""
		This exception is meant to be raised when an illegal file type (not .txt) is attempted to be loaded
		:param msg: A string of the message that may be entered (it is None by default, so nothing needs to be entered)
		"""
		self.msg = msg

class IllegalFileType(Exception):

	def __init__(self, msg=None):
		"""
		This exception is meant to be raised when an illegal file type (not .txt) is attempted to be loaded
		:param msg: A string of the message that may be entered (it is None by default, so nothing needs to be entered)
		"""

		self.msg = msg


class DLinkedListNode:
	def __init__(self, initData, initNext, initPrevious):
		self.data = initData
		self.next = initNext
		self.previous = initPrevious

		if (initPrevious != None):
			initPrevious.next = self
		if (initNext != None):
			initNext.previous = self


	def __str__(self):
		return "%s" % (self.data)

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def getPrevious(self):
		return self.previous

	def setData(self, newData):
		self.data = newData

	def setNext(self, newNext):
		self.next = newNext

	def setPrevious(self, newPrevious):
		self.previous= newPrevious

class DLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	def __str__(self):
		s = "[ "
		current = self.head
		while current != None:
			s += "%s " % (current)
			current = current.getNext()
		s += "]"
		return s

	def isEmpty(self):
		return self.size == 0

	def length(self):
		return self.size

	def getHead(self):
		return self.head

	def getTail(self):
		return self.tail

	def search(self, item):
		current = self.head
		found = False
		while current != None and not found:
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()
		return found

	def index(self, item):
		current = self.head
		found = False
		index = 0
		while current != None and not found:
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()
				index = index + 1
		if not found:
			index = -1
		return index

	def add(self, item):
		temp = DLinkedListNode(item, self.head, None)
		if self.head != None:
			self.head.setPrevious(temp)
		else:
			self.tail = temp
		self.head = temp
		self.size += 1

	def append(self, item):
		temp = DLinkedListNode(item, None, None)
		if (self.head == None):
			self.head = temp
		else:
			self.tail.setNext(temp)
			temp.setPrevious(self.tail)
		self.tail = temp
		self.size +=1

	def remove(self, item):
		current = self.head
		previous = None
		found = False
		while not found:
			if current.getData() == item:
				found = True
			else:
				previous = current
				current = current.getNext()
		if previous == None:
			self.head = current.getNext()
		else:
			previous.setNext(current.getNext())
		if (current.getNext() != None):
			current.getNext().setPrevious(previous)
		else:
			self.tail = previous
		self.size -= 1

	def removeitem(self, current):
		previous = current.getPrevious()
		if previous == None:
			self.head = current.getNext()
		else:
			previous.setNext(current.getNext())
		if (current.getNext() != None):
			current.getNext().setPrevious(previous)
		else:
			self.tail=previous
		if previous:
			self.curr = previous.getNext()
		else:
			self.curr = None
		self.size -= 1

	def insert(self, current, item, where=0):
		"""
		Insert a new node with a specific line in the specified location
		:param current: the current Node
		:param item: string of the line we want to insert
		:param where: accepts 0 or 1 (implemented as an exception),
		:return:
		"""
		# You write this code
		# NOTE: there is an extra parameter here
		# Where = 0 (before current)
		# Where = 1 (after current)

		#TODO
		# - put some kind of exception for invalid current (i.e line was never found)
		# -- Because of this, there cannot be a case if the double-linked list is empty

		assert where == 0 or where == 1

		currentNode = self.head
		previousNode = None
		found = False

		while currentNode != None and not found:

			if currentNode == current:
				found = True
			else:
				previousNode = currentNode
				currentNode = currentNode.getNext()


		# Now we must also consider the case if the list is empty (for the exception later)
		if self.isEmpty():
			found = True

		if not found:
			raise ItemError

		# Now we must check if the user want's to put it before the currentNode or after
		# - currentNode must also be not None (i.e that indicates the list is empty)
		if where == 1 and currentNode != None:
			# If its after the line, then make our currentNode the initPrevious, and currentNode.getNext() the initNext
			initPrevious = currentNode
			initNext = currentNode.getNext()


		else:
			# Since an exception will handle any other value than 0, use else here
			# If its before the line, then our initPrevious should be our previous
			initPrevious = previousNode
			initNext = currentNode

		newNode = DLinkedListNode(item, initNext, initPrevious)

		# Check if Node is the new tail
		if initNext == None:
			self.tail = newNode

		# Check if Node is the head
		if initPrevious == None:
			self.head = newNode

		# Increment the size
		self.size += 1

class TextFile:
	# This is the TextFile class

	def __init__(self,name):
		"""
		create a TextFile, recording the name of the file read
		:param name: string name of text file
		"""

		self.__name = name
		self.__fileList = DLinkedList()
		self.__currentNode = None
		self.__currentLine = 0
		self.__lineCount = 0

	def load(self,name):
		"""
		Loads the initalized textfile
		:param name: string name of text file
		:return: None
		"""

		assert isinstance(name,str)
		# TODO: Handle FileNotFoundError, it is raised when the file does not exist
		self.__fileList = DLinkedList()

		# Open the file in both reading and writing mode
		if name[-4:] != '.txt':
			raise IllegalFileType

		try:
			with open(name , 'r') as file:

				# Read the file and insert all the contents into the DlinkedList
				fileContent = file.read()

			tempList =fileContent.splitlines( )

			for line in tempList:
				self.__fileList.append(line)

			self.__currentNode = self.__fileList.getTail()
			self.__currentLine = self.__fileList.length()
			self.__name = name

		except FileNotFoundError:
			raise FileNotFoundError

	def write(self, name=None):
		"""
		Saves the file as a new one or over-writes the same file
		:param name: name of the file we are writing to
		:return:
		"""
		if name[-4:] != '.txt':
			raise IllegalFileType


		startNode = self.__fileList.getHead()
		try:
			with open(name, 'w') as file:

				# Only run this while loop if the currentNode is not (i.e the list has at least one element)
				while startNode != None:
					file.write(startNode.getData() + '\n')
					startNode = startNode.getNext()

		except OSError:
			raise OSError

	def add(self,where):
		"""
		Adds lines after the previously inserted line (which is the current line) until the user has entered a
		blank line

		The new current line becomes the last line added with this function (it will increment the current line number
		based on how many more new lines are added)

		:param where: accepts integers 0 or 1. 0 = insert before (used for insert command),
		1 = insert after (used for add command)

		(exception will be raised in the DlinkedList's insert method)
		:return: None
		"""
		assert where == 0 or where == 1

		# get the current line
		currentLine = self.__currentLine


		# Get the starting node based on the current line
		currentNode = self.__currentNode

		# Make a while loop asking for the user's input each time to insert a new line
		finishAdding = False

		while not finishAdding:
			line = input()
			if len(line.strip()) > 0:
				if currentNode == None:
					self.__fileList.append(line)
					currentNode = self.__fileList.getHead()
					where = 1

				else:
					self.__fileList.insert(currentNode,line,where)

					if where == 1:
						currentNode = currentNode.getNext()

				currentLine += 1
			else:
				finishAdding = True

		# change the current line to the new line based on the line number (this will also update the line number too)
		if where == 1:
			self.__currentLine = currentLine
			self.__currentNode = currentNode

		else:
			self.__currentNode = currentNode.getPrevious()
			self.__currentLine = currentLine - 1

	def delete(self, offset):
		"""
		deletes the specified number of lines from the current line and
		:param offset: The number of lines
		:return:
		"""
		assert isinstance(offset,int)

		if self.__fileList.isEmpty():
			raise EmptyFileError

		oldCurrentLine = self.__currentLine
		backwards = offset < 0

		endPoint = self.__currentLine + offset
		# Check if the end point is below 1 or above file size
		if endPoint < 1:
			endPoint = 1

		elif endPoint > self.__fileList.length():
			endPoint = self.__fileList.length()

		linesToDelete = abs(endPoint - oldCurrentLine) + 1

		# CASE I: Beginning lines of the file are removed
		# - Can happen if the endPoint is 1 and we traverse backwards
		# - Can also happen if the startPoint is 0 and we traverse forwards

		if endPoint == 1 or oldCurrentLine == 1:
			newLine = linesToDelete + 1


		# CASE II: End lines are removed of the list
		elif endPoint == self.__fileList.length() or oldCurrentLine == self.__fileList.length():

			newLine = self.__fileList.length() - linesToDelete

		# CASE III (General Case): If it is removed anywhere in between from the list
		elif backwards:
			newLine = oldCurrentLine + 1


		else:
			newLine = endPoint + 1



		oldLength = self.__fileList.length()
		# Check if the newLine is below above the number of items in the list or below 1

		if newLine <= self.__fileList.length() and newLine >= 1:
			newNode = self.__getNodeFromLine(newLine)

		else:
			newNode = None

		oldCurrentNode = self.__currentNode


		deletedLines = 0
		while oldCurrentNode != None and oldCurrentNode != newNode and deletedLines <= abs(offset):
			self.__fileList.removeitem(oldCurrentNode)

			if backwards:
				oldCurrentNode = oldCurrentNode.getPrevious()

			else:
				oldCurrentNode = oldCurrentNode.getNext()

			deletedLines += 1


		if (backwards and endPoint == 1) or (not backwards and oldCurrentLine == 1):
			currentLine= 1

		elif (not backwards and endPoint == oldLength) or (backwards and oldCurrentNode == oldLength):
			currentLine = self.__fileList.length()

		elif newNode == None:
			currentLine = 0


		elif backwards:
			currentLine = endPoint

		else:
			currentLine = oldCurrentLine

		self.__currentLine = currentLine
		self.__currentNode = newNode



	def print(self,offset):
		"""
		displays the lines onto the console with the appropriate numbers
		:param offset: The number of lines from the currentLine
		:return:
		"""
		assert isinstance(offset, int)
		if not self.__fileList.isEmpty():

			# Get the end line based on if the offset is negative or positive

			if offset > 0:
				beginningLine = self.__currentLine
				endLine = self.__currentLine + offset

			else:
				beginningLine = self.__currentLine + offset
				endLine = self.__currentLine

			if endLine > self.__fileList.length():
				endLine = self.__fileList.length()

			elif beginningLine < 1:
				beginningLine = 1

			currentNode = self.__getNodeFromLine(beginningLine)

			lineSpacing = 2

			while beginningLine <= endLine:
				strLine = f'{beginningLine}: {currentNode}'
				print(f'%{lineSpacing + len(strLine)}s' % strLine)
				beginningLine += 1
				currentNode = currentNode.getNext()

			self.linenum(endLine)

	def linenum(self,line):
		"""
		checks if the line number is closer to the end, to the beginning or to the current line number
		if its closer to the end, then traverse backwards from the end by the amount of steps its close to the end by
		if its close to the current then start from the current and traverse forward if it is more than the current or
		backwards if it is less
		if it is closer to the head then start from the head and traverse forward
		:param line: the integer of the line number
		:return: None
		"""
		assert isinstance(line, int)
		current = self.__getNodeFromLine(line)

		self.setCurrent(current)
		self.setLine(line)

	def setCurrent(self,current):
		"""
		Sets the self.__currentNode to the current entered as an argument
		:param current: DLinkedListNode object
		:return:
		"""
		self.__currentNode = current

	def setLine(self,line):
		"""
		Sets the self.__currentLine to line
		:param line: integer of the line number
		:return: None
		"""

		self.__currentLine = line

	def getCurrent(self):
		return self.__currentNode

	def getLine(self):
		return self.__currentLine


	def __getNodeFromLine(self,line):
		"""
		checks if the line number is closer to the end, to the beginning or to the current line number
		if its closer to the end, then traverse backwards from the end by the amount of steps its close to the end by
		if its close to the current then start from the current and traverse forward if it is more than the current or
		backwards if it is less
		if it is closer to the head then start from the head and traverse forward
		:param line: the integer of the line number
		:return: DlinkedlistNode
		"""
		assert isinstance(line, int)

		if not (0 < line <= self.__fileList.length()):
			raise IllegalLine

		# Check if we need to even change the current line (i.e if the user enters the same line then there is no point)

		# 1 Check how many steps the line number is from the 3 points of reference mentioned above

		# currentLine can either be backwards traversal or forward traversal
		currentSteps = line - self.__currentLine

		# The head is the first line (traverse forward always)
		headSteps = line - 1

		# The tail is always the last line (traverse backwards)
		tailSteps = line - self.__fileList.length()

		# Check which mode of traversal will take the least amount of steps

		# - current should be point of reference
		if abs(currentSteps) <= headSteps and abs(currentSteps) <= abs(tailSteps):
			startNode = self.__currentNode
			traversedLines = abs(currentSteps)
			isBackwards = currentSteps < 0

		elif headSteps <= abs(currentSteps) and headSteps <= abs(tailSteps):
			startNode = self.__fileList.getHead()
			traversedLines = headSteps
			isBackwards = False
		else:
			startNode = self.__fileList.getTail()
			traversedLines = abs(tailSteps)
			isBackwards = True

		current = startNode

		# Now traverse the list to set the new current
		for lineNumber in range(traversedLines):

			if isBackwards:
				current = current.getPrevious()

			else:
				current = current.getNext()


		return current

	def search(self,text,where):
		"""
		Searches starting from the currentNode to the next node until the appropriate node is found
		:param text: str of text to find
		:param where: 0 for reverse search 1 for forward
		:return: None
		"""

		assert where == 0 or where == 1 and isinstance(text,str)

		if where == 1:
			searchedLine = self.__searchForwards(text)

		else:
			searchedLine = self.__searchBackwards(text)

		if searchedLine != self.__currentLine:
			self.linenum(searchedLine)


	def __searchForwards(self,text):
		"""
		Searches starting from the currentNode to the next node until the appropriate node is found (forward)
		:param text: str of text to find
		:return: None
		"""
		assert isinstance(text,str)
		currentNode = self.__currentNode
		searchNode = currentNode
		currentLine = self.__currentLine
		searchLine = currentLine
		found = False
		notExist = False

		if not self.__fileList.isEmpty():
			while not found and not notExist:
				searchNode = searchNode.getNext()
				searchLine += 1

				# Loop the searchNode pointer around to the beginning of the list if the searchNode points to None
				if searchNode == None:
					searchLine = 1
					searchNode = self.__fileList.getHead()

				if searchNode == currentNode:
					notExist = True

				elif text in searchNode.getData():
					found = True


		return searchLine

	def __searchBackwards(self,text):
		"""
		Searches starting from the currentNode to the next node until the appropriate node is found (backwards)
		:param text: str of text to find
		:return: None
		"""
		assert isinstance(text, str)
		currentNode = self.__currentNode
		searchNode = currentNode
		currentLine = self.__currentLine
		searchLine = currentLine
		found = False
		notExist = False

		if not self.__fileList.isEmpty():
			while not found and not notExist:
				searchNode = searchNode.getPrevious()
				searchLine -= 1

				# Loop the searchNode pointer around to the beginning of the list if the searchNode points to None
				if searchNode == None:
					searchLine = self.__fileList.length()
					searchNode = self.__fileList.getTail()

				if searchNode == currentNode:
					notExist = True

				elif text in searchNode.getData():
					found = True


		return searchLine

	def sort(self):
		"""
		Uses selection sort to sort the file in ascending order
		:return: None
		"""
		currentNode = self.__fileList.getHead()

		while currentNode != None:
			minNode = currentNode
			minChecker = currentNode
			swap = False
			while minChecker != None:

				if minChecker.getData() < minNode.getData():
					minNode = minChecker
					swap = True
				minChecker = minChecker.getNext()

			if swap:
				minData = minNode.getData()
				currentNodeData = currentNode.getData()
				minNode.setData(currentNodeData)
				currentNode.setData(minData)

			currentNode = currentNode.getNext()

		self.linenum(self.__fileList.length())

	def setName(self,name):
		"""
		Sets the file's name
		:param name: name of file with .txt extension
		:return: None
		"""
		self.__name = name

	def getName(self):
		"""
		Get the file's name
		:return: name of file with .txt extension [str]
		"""
		return self.__name

	def replace(self,text1,text2):
		"""
		Replaces the word in the current line (text1) with text2
		:param text1: str of word in current line
		:param text2: str of word to replace with
		:return: None
		"""

		if not self.__fileList.isEmpty():
			line = self.__currentNode.getData()
			newLine = line.replace(text1,text2)
			self.__currentNode.setData(newLine)
def getCommand():
	"""
	Gets a user's input and returns it as a command list
	:return: list
	"""
	command = input('>')
	return shlex.split(command)

def printCommand(command,tf):
	"""
	Handle the print command
	:param command: List of the commands
	:param tf: TextFile class object
	:return: None
	"""

	if len(command) > 1:
		line = command[1].strip()

	else:
		line = 0

	if (line != 0 and not line.strip('-').isdigit()) or len(command) > 2:
		raise InvalidArgument

	tf.print(int(line))

def deleteCommand(command,tf):
	"""
	Handle the print command
	:param command: List of the commands
	:param tf: TextFile class object
	:return: None
	"""

	if len(command) > 1:
		line = command[1].strip()

	else:
		line = 0

	if (line != 0 and not line.strip('-').isdigit()) or len(command) > 2:
		raise InvalidArgument

	tf.delete(int(line))

def handleSearchCommands(command,tf):
	"""
	Handle the search command
	:param command: List of the commands (command[0] can be / for forward or ? for backward)
	:param tf: TextFile class object
	:return: None
	"""

	searchMode = command[0].strip()
	lineToSearch = command[1].strip()

	if not searchMode in ('/','?') and len(command) != 2:
		raise InvalidArgument

	if searchMode == '/':
		tf.search(lineToSearch,1)

	else:
		tf.search(lineToSearch, 1)

	tf.print(0)

def handleCommands(command):
	"""
	Decides which command the user chose based on the first index of the list
	:param command: command list
	:return: str of first index
	"""
	if len(command) > 0:
		possibleCommands = ['a','d','i','l','p','q','r','s','w','/','?']
		commandName = command[0].strip().lower()

		if commandName not in possibleCommands and not commandName.strip('-').isdigit():
			raise InvalidCommand

		return commandName

def loadCommand(command,tf):
	"""
	Handles the load command
	:param command: command list
	:param tf: TextFile class object
	:return: None
	"""

	if not len(command) == 2:
		raise InvalidArgument

	name = command[1]

	assert isinstance(name,str)

	tf.load(name)
	print(name, f'({tf.getLine()})')


def saveCommand(command, tf):
	"""
	Handles the save command
	:param command: command list
	:param tf: TextFile class object
	:return: None
	"""

	if not len(command) == 2:
		raise InvalidArgument

	if len(command) == 2:
		name = command[1]

		assert isinstance(name, str)

	else:
		name = tf.getName()
	tf.write(name)
	print(name, f'({tf.getLine()})')

def replaceCommand(command,tf):
	"""
	Handles the replace command
	:param command: command list
	:param tf: TextFile class object
	:return: None
	"""

	if not (1 < len(command) <= 3):
		raise InvalidArgument

	line1 = command[1]

	if len(command) == 2:
		tf.replace(line1,'')

	else:
		line2 = command[2]
		tf.replace(line1,line2)

	tf.print(0)

def main():

	print('Welcome to ed379')

	notQuit = True
	defaultName = 'untitled.txt'
	tf = TextFile(defaultName)

	while notQuit:

		command = getCommand()
		currentLine = tf.getLine()

		try:
			commandName = handleCommands(command)

			if commandName == 'a' and len(command) == 1:
				tf.add(1)

			elif commandName == 'i' and len(command) == 1:
				tf.add(0)

			elif commandName in ('/','?'):
				handleSearchCommands(command,tf)

			elif commandName == 'p':
				printCommand(command,tf)

			elif commandName == 's' and len(command) == 1:
				tf.sort()

			elif commandName == 'd':
				deleteCommand(command,tf)

			elif commandName == 'r':
				replaceCommand(command,tf)

			elif commandName == 'l':
				loadCommand(command,tf)

			elif commandName == 'w':
				saveCommand(command,tf)

			elif commandName == None:

				try:
					tf.linenum(currentLine + 1)
					tf.print(0)

				except IllegalLine:
					pass

			elif commandName.strip('-').isdigit():
				tf.linenum(int(commandName))

			elif commandName == 'q' and len(command) == 1:
				notQuit = False

			else:
				raise InvalidCommand


		except FileNotFoundError:
			print('File not found')

		except IllegalFileType:
			print('Illegal Filetype, only .txt is acceptable')

		except InvalidArgument:
			print('Invalid Argument')

		except InvalidCommand:
			print('Invalid Command!')

		except EmptyFileError:
			print('Cannot perform this operation on an empty file')

		except IllegalLine:
			print('Illegal line position')

	print('Good-bye')

main()




# if __name__ == '__main__':
#
# 		tf = TextFile('A3-sample.txt')
# 		tf.load('A3-sample.txt')
# 		tf.linenum(2)
# 		tf.add(0)
# 		tf.linenum(10)
# 		tf.print(100)
# 		tf.print(1)
# 		# tf.search('it was the worst of times',0)
# 		# tf.print(0)
# 		# tf.sort()
# 		# tf.linenum(1)
# 		# tf.print(100)



