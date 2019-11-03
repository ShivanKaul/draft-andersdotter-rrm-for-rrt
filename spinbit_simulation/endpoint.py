class Endpoint(object):
	def __init__(self, initial_spin, probability):
		self._cur_spin = initial_spin 
		self._probability = probability

	# getter
	@property
	def cur_spin(self):
		return self._cur_spin

	# setter
	@cur_spin.setter
	def cur_spin(self, value):
		pass