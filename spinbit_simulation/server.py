from endpoint import Endpoint
import random


class Server(Endpoint):
	# With probability Q, we set incorrectly

	def usual_operation(self, new_value):
		# reflects
		return new_value
