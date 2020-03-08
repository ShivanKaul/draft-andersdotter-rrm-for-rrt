# Spin Bit Simulation

Run `make` to do a `clean` and `pip install` and then run `make run` to run the simulation.

You can use variables P and Q in the call to `run_simulation()` in `run_simulation.py` as referred to in the draft to customize the simulation run. You can also change `length_of_path` and `total_ticks`. `run_simulation.py` script comes with two pre-defined lying functions - `lie_on_every_packet` and `lie_on_edge`. You can supply these functions to `run_simulation.py` to modify behaviour. 


Note that we are only simulating logical flow of spinbits without any consideration for packet loss etc. Also, we are only concerned with the spinbit part of the packet. 