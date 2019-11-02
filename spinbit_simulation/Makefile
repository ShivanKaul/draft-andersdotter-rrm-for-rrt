.PHONY: clean install run

all: clean install
	
clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +

install:
	pip install -r requirements.txt

run:
	python run_simulation.py

