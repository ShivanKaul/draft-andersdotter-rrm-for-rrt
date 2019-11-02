from endpoint import Endpoint
import random


class Client(Endpoint):
	# setter - this is what inverts the spin
	# With probability P, we set incorrectly
	@Endpoint.cur_spin.setter
	def cur_spin(self, cur_spin):
		# invert
		should_lie = random.random() < self._probability
		self._cur_spin = cur_spin if should_lie else abs(1-cur_spin) 
