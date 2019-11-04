from endpoint import Endpoint
import random


class Client(Endpoint):
	# With probability P, we set incorrectly

	def usual_operation(self, new_value):
		# invert
		return abs(1-new_value)
