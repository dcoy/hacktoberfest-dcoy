class world:
	def __init__(self):
		self.first()
	def first(self):
		print "World !!"

class hello(world):
	def __init__(self):
		print "Hello",
		world.__init__(self)

pr= hello()