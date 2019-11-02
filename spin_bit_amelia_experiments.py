import time
import random as rd

class Server(object):
    def __init__(self, initial_spin, probability):
        self._curSpin = initial_spin
        self._probability = probability

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

    # This is basically maintaining a path. 
    def addValueToPath(self, value):
        self._path[self.curIndex % self._maxSize] = value
        self.curIndex += 1
        return self._path[-1]


class Observer:
    def __init__(self):
        self.measurements = []
    # measurements are indexed by tick i.e. 
    # for 3 ticks the measurement list could look like [0,0,1]

    def measureRTT(self):
        print("Final RTT is")
        a = self.measurements
        badCounterVector = []
        counterOfOnes = 0
        counterOfZeros = 0
        for i in range(len(a)):
            if a[i] == 1:
                counterOfOnes = counterOfOnes+1
                badCounterVector.append(counterOfZeros)
                counterOfZeros = 0
            else:
                counterOfZeros = counterOfZeros + 1 
                badCounterVector.append(counterOfOnes)
                counterOfOnes = 0
        cleanCounterVector = [x for x in badCounterVector if x!=0]
        # removing first value in cleanCounterVector since it only
        # contains half a RTT in either case.
        return sum(cleanCounterVector[1:])/len(cleanCounterVector[1:]) # not implemented yet

    def addMeasurement(self, path):
        # for a given path, get the midpoint
        midpt = path.maxSize // 2
        num = path.getValueAtIndex(midpt)
        if num != None:
            # the path might not be full yet
            self.measurements.append(num)

# TODO: omission of inversion at edge, omission of reflection at edge
# lying at every bit.
# P = probability of client lying at reflection
# Q = probability of server lying at inversion
# P2 = probability of client lying at each transmission (I propose)
def runSimulation(P, Q, lengthOfPath, totalTicks):
    clientToServerPath = Path(lengthOfPath)
    serverToClientPath = Path(lengthOfPath)

    client = Client(0, P)
    server = Server(0, Q)
    observer = Observer()

    ticks = 0

    while (ticks < totalTicks):
        bitReachingServer = clientToServerPath.addValueToPath(client.curSpin)
        bitReachingClient = serverToClientPath.addValueToPath(server.curSpin)

        # set value for next tick
        if bitReachingServer != None:
            # DEBUG code: print(ticks, bitReachingServer)
            server.curSpin = bitReachingServer
        if bitReachingClient != None:
            client.curSpin = bitReachingClient

        # C --- S
        # print("Client -> "), 
        # print(clientToServerPath.path),
        # print("-> Server") 

        # print("Client <- "), 
        # print(list(reversed(serverToClientPath.path))),
        # print("<- Server")
        # print('\n')
        
        observer.addMeasurement(clientToServerPath)

        ticks += 1
        # time.sleep(0.5)
        
    print(observer.measureRTT())
    

    
runSimulation(0, 0.2, 5, 500)
