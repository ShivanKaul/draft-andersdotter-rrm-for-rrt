import random
from client import Client
from server import Server
from observer import Observer
from path import Path

def lie_on_every_packet(cur_spin, new_spin, probability):
	should_lie = random.random() < probability
	return new_spin if not should_lie else abs(1-new_spin)

def lie_on_edge(cur_spin, new_spin, probability):
	should_lie = (random.random() < probability) and cur_spin != new_spin
	return new_spin if not should_lie else abs(1-new_spin)


def run_simulation(P=0, Q=0, lying_function=lie_on_every_packet, length_of_path=5, total_ticks=50):

	client_to_server_path = Path(length_of_path, "Client", "Server")
	server_to_client_path = Path(length_of_path, "Server", "Client")

	client = Client(0, P, lying_function)
	server = Server(0, Q, lying_function)
	observer = Observer()

	current_tick = 1

	while (current_tick <= total_ticks):
		# add_packet_to_path() pops off the bit that has 
		# reached the end of the path
		bit_reaching_server = client_to_server_path.add(client.cur_spin)
		bit_reaching_client = server_to_client_path.add(server.cur_spin)

		# update value of spin bit for client and server
		# this will be set next tick
		client.cur_spin = bit_reaching_client
		server.cur_spin = bit_reaching_server

		print("Tick:"),
		print(current_tick)

		client_to_server_path.pretty_print()
		server_to_client_path.pretty_print(True)
		
		# measurements are sampled from midpoint of path
		observer.add_measurement(client_to_server_path)

		current_tick += 1

	print("Final RTT is %.2f") % observer.measure_rtt()

# P and Q are [0,1]
run_simulation(0.5, 0, lie_on_edge, 5, 50)
