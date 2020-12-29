# Feel free to add new properties and methods to the class.
class MinMaxStack:
	def __init__(self):
		self.stack = []
		self.min_stack = []
		self.max_stack = []

    def peek(self):
        if len(self.stack) == 0:
			return None
		else:
			return self.stack[-1]

    def pop(self):
        if len(self.stack) == 0:
			return
		else:
			number = self.stack[-1]
			self.stack.pop()
			if self.min_stack[-1] == number:
				self.min_stack.pop()
			if self.max_stack[-1] == number:
				self.max_stack.pop()
		return number

    def push(self, number):
        self.stack.append(number)
		if len(self.max_stack) == 0:
			self.max_stack.append(number)
		else:
			if self.max_stack[-1] <= number:
				self.max_stack.append(number)
		if len(self.min_stack) == 0:
			self.min_stack.append(number)
		else:
			if self.min_stack[-1] >= number:
				self.min_stack.append(number)

    def getMin(self):
        if len(self.min_stack) == 0:
			return None
		else:
			return self.min_stack[-1]
		
    def getMax(self):
        if len(self.max_stack) == 0:
			return None
		else:
			return self.max_stack[-1]
