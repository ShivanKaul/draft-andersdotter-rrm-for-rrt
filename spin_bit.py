class Server(object):
	def __init__(self, initial_spin):
		self._curSpin = initial_spin 

	# getter
	@property
	def curSpin(self):
		return self._curSpin

	# setter
	@curSpin.setter
	def curSpin(self, value):
		# reflects
		self._curSpin = value

class Client(object):
	def __init__(self, initial_spin, probability):
		self._curSpin = initial_spin 
		self._probability = probability

	# getter
	@property
	def curSpin(self):
		# TODO: Lie with probability
		return self._curSpin

	# setter - this is what inverts the spin
	@curSpin.setter
	def curSpin(self, curSpin):
		# invert
		self._curSpin = abs(1-curSpin)
	

class Path:
	def __init__(self, maxSize):
		self._maxSize = maxSize
		# a list of Nones of size maxSize to begin with
		self._path = [None for x in range(maxSize)]
		self.curIndex = 0

	@property
	def maxSize(self):
		return self._maxSize

	@property
	def path(self):
		return self._path
	
	def getValueAtIndex(self, index):
		return self._path[index]

	# bug here :( - this is basically maintaining a path. 
	# every time the path is full we add new value 
	# to curIndex % totalSize.
	# Also if the path is full then we must 'pop' an element
	# that will be fed into a client/server
	def addValueToPath(self, value):
		if self.curIndex >= self._maxSize:
			popped = self._path[-1]
		else:
			popped = None
		self._path[self.curIndex % self._maxSize] = value
		self.curIndex += 1
		return popped


class Observer:
	def __init__(self):
		self.measurements = []
	# measurements are indexed by tick i.e. 
	# for 3 ticks the measurement list could look like [0,0,1]

	def measureRTT(self):
		print("Final RTT is")
		return None # not implemented yet

	def addMeasurement(self, path):
		# for a given path, get the midpoint
		midpt = path.maxSize // 2
		num = path.getValueAtIndex(midpt)
		if num != None:
			# the path might not be full yet
			self.measurements.append(num)



def runSimulation(P, Q, lengthOfPath, totalTicks):
	clientToServerPath = Path(lengthOfPath)
	serverToClientPath = Path(lengthOfPath)

	client = Client(0, P)
	server = Server(0)
	observer = Observer()

	ticks = 0

	while (ticks < totalTicks):
		bitReachingServer = clientToServerPath.addValueToPath(client.curSpin)
		bitReachingClient = serverToClientPath.addValueToPath(server.curSpin)
		if bitReachingServer != None:
			# DEBUG code: print(ticks, bitReachingServer)
			server.curSpin = bitReachingServer
		if bitReachingClient != None:
			client.curSpin = bitReachingClient

		# C --- S
		print("Client -> "), 
		print(clientToServerPath.path),
		print("-> Server") 

		print("Client <- "), 
		print(list(reversed(serverToClientPath.path))),
		print("<- Server")
		print('\n')
		
		observer.addMeasurement(clientToServerPath)

		ticks += 1

	print(observer.measureRTT())

runSimulation(0.2, 0.2, 5, 20)
