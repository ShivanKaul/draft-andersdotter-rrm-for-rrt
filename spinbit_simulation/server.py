from endpoint import Endpoint
import random


class Server(Endpoint):
	# setter
	# With probability Q, we set incorrectly
	@Endpoint.cur_spin.setter
	def cur_spin(self, cur_spin):
		# reflects
		should_lie = random.random() < self._probability
		self._cur_spin = abs(1-cur_spin) if should_lie else cur_spin
