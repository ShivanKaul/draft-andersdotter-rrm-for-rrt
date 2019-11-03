from client import Client
from server import Server
from observer import Observer
from path import Path

def run_simulation(P=0, Q=0, length_of_path=5, total_ticks=50):

	client_to_server_path = Path(length_of_path)
	server_to_client_path = Path(length_of_path)

	client = Client(0, P)
	server = Server(0, Q)
	observer = Observer()

	current_tick = 1

	while (current_tick <= total_ticks):
		bit_reaching_server = client_to_server_path.add_packet_to_path(client.cur_spin)
		bit_reaching_client = server_to_client_path.add_packet_to_path(server.cur_spin)

		# update value of spin bit for client and server
		server.cur_spin = bit_reaching_server
		client.cur_spin = bit_reaching_client

		# C --- S
		print("Tick:"),
		print(current_tick)
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

		current_tick += 1

	print("Final RTT is %.2f") % observer.measure_rtt()

# P and Q are [0,1]
run_simulation(0.8, 0, 5, 50)
