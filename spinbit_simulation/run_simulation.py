from client import Client
from server import Server
from observer import Observer
from path import Path

def run_simulation(P, Q, length_of_path, total_ticks):

	client_to_server_path = Path(length_of_path)
	server_to_client_path = Path(length_of_path)

	client = Client(0, P)
	server = Server(0, Q)
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
run_simulation(0, 0, 5, 50)
