.PHONY: all install lint test format

all: lint test

install:
	pip install -r requirement.txt

compile:
	pip-compile requirements.in

upgrade:
	pip-compile --upgrade requirements.in

lint:
	black --check .

test:
	echo "no tests lol"

format:
	black .
