class Endpoint(object):
	def __init__(self, initial_spin, probability, lying_function):
		self._cur_spin = initial_spin 
		self._probability = probability
		self._lying_function = lying_function

	# overriden by client or server
	def usual_operation(self, value):
		pass

	# getter
	@property
	def cur_spin(self):
		return self._cur_spin

	# setter
	@cur_spin.setter
	def cur_spin(self, new_value):
		if new_value is not None:
			# what would have been the value if we didn't lie?
			no_lie_next_spin = self.usual_operation(new_value)
			# apply lying function
			next_spin = self._lying_function(
				self._cur_spin, 
				no_lie_next_spin, 
				self._probability)
			self._cur_spin = next_spin

	