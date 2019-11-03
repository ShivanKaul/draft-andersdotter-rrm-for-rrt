class Path:
	def __init__(self, max_size):
		self._max_size = max_size
		# a list of Nones of size maxSize to begin with
		self._path = [None for x in range(max_size)]
		self.cur_index = 0

	@property
	def max_size(self):
		return self._max_size

	@property
	def path(self):
		return self._path
	
	def get_spinbit_at_position(self, index):
		return self._path[index]

	# This is basically maintaining a path. 
	def add_packet_to_path(self, value):
		self._path[self.cur_index % self._max_size] = value
		self.cur_index += 1
		return self._path[-1]
