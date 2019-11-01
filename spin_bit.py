# install packages with pip install

import statistics 
import random

class Server(object):
	def __init__(self, initial_spin):
		self._cur_spin = initial_spin 

	# getter
	@property
	def cur_spin(self):
		return self._cur_spin

	# setter
	@cur_spin.setter
	def cur_spin(self, value):
		# reflects
		self._cur_spin = value

class Client(object):
	def __init__(self, initial_spin, probability):
		self._cur_spin = initial_spin 
		self._probability = probability

	# getter
	@property
	def cur_spin(self):
		return self._cur_spin

	# setter - this is what inverts the spin
	# With probability P, we set incorrectly
	@cur_spin.setter
	def cur_spin(self, cur_spin):
		# invert
		should_lie = random.random() < self._probability
		self._cur_spin = cur_spin if should_lie else abs(1-cur_spin) 
	
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
	
	def get_value_at_index(self, index):
		return self._path[index]

	# This is basically maintaining a path. 
	def add_value_to_path(self, value):
		self._path[self.cur_index % self._max_size] = value
		self.cur_index += 1
		return self._path[-1]


class Observer:
	def __init__(self):
		self._measurements = []
		self.rtts = []
		self.cur_train = -1
		self.edge_detected = False
		self.ticks_between_edges = 0
	# measurements are indexed by tick i.e. 
	# for 3 ticks the measurement list could look like [0,0,1]

	@property
	def measurements(self):
		return self._measurements
	
	def measure_rtt(self):
		print("Measurements recorded: %s" % self._measurements)
		print("RTTs: %s" % self.rtts)
		return statistics.mean(self.rtts) if len(self.rtts) > 0 else 0

	def add_measurement(self, path):
		# for a given path, get the midpoint
		midpt = path.max_size // 2

		num = path.get_value_at_index(midpt)
		if num != None:
			# the path might not be full yet
			self._measurements.append(num)

			if self.cur_train == -1:
				# print("first measurement")
				self.cur_train = num
			elif num != self.cur_train:
				# print("edge transition detected")
				# add to rtt if edge was previously detected
				if self.edge_detected:
					self.rtts.append(self.ticks_between_edges)
				else: # edge detected
					self.edge_detected = True
				# reset tick count
				self.ticks_between_edges = 0
				# reset current train
				self.cur_train = num
			
			self.ticks_between_edges += 1


def run_simulation(P, length_of_path, total_ticks):

	client_to_server_path = Path(length_of_path)
	server_to_client_path = Path(length_of_path)

	client = Client(0, P)
	server = Server(0)
	observer = Observer()

	ticks = 1

	while (ticks <= total_ticks):
		bit_reaching_server = client_to_server_path.add_value_to_path(client.cur_spin)
		bit_reaching_client = server_to_client_path.add_value_to_path(server.cur_spin)

		# set value for next tick
		if bit_reaching_server != None:
			server.cur_spin = bit_reaching_server
		if bit_reaching_client != None:
			client.cur_spin = bit_reaching_client

		# C --- S
		print("Tick:"),
		print(ticks)
		print("Client -> "), 
		print(client_to_server_path.path),
		print("-> Server") 

		print("Client <- "), 
		# to make it slightly easier to read, 
		# we reverse path before printing
		print(list(reversed(server_to_client_path.path))),
		print("<- Server")
		print('\n')
		
		# measurements are sampled from midpoint of path
		observer.add_measurement(client_to_server_path)

		ticks += 1

	print("Final RTT is %f") % observer.measure_rtt()

# P is [0,1]
run_simulation(0, 5, 50)
