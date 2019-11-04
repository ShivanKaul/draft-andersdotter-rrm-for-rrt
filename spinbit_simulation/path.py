from collections import deque

class Path:
	def __init__(self, max_size, path_from, path_to):
		self._max_size = max_size
		# a list of Nones of size maxSize to begin with
		noneList = [None for x in range(self._max_size)]
		self._path = deque(noneList)
		self._path_from = path_from
		self._path_to = path_to

	def pretty_print(self, reverse=False):
		if not reverse:
			print("%s -> " % self._path_from), 
			print(self.path),
			print("-> %s" % self._path_to)
		else:
			print("%s <- " % self._path_to), 
			print(list(reversed(self.path))),
			print("<- %s" % self._path_from)


	@property
	def max_size(self):
		return self._max_size

	@property
	def path(self):
		return list(self._path)
	
	def get_spinbit_at_position(self, index):
		return self._path[index]

	# Adds to the path. 
	# The last index is what the endpoint is processing
	# Returns the packet reaching the to-endpoint
	def add(self, value):
		# what is reaching the to-endpoint
		# the second-last item in the deque is actually 
		# what will be reaching the endpoint after this addition
		toReturn = self._path[-2]
		self._path.rotate(1)
		self._path[0] = value

		return toReturn
