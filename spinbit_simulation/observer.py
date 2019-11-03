import statistics 


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

		num = path.get_spinbit_at_position(midpt)
		if num != None:
			# the path might not be full yet
			self._measurements.append(num)

			# Detect RTT by keeping track of edge transitions
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