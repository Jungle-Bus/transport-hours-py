all: deps test docs

deps:
	pip install -r requirements-dev.txt

test:
	python -m unittest discover

docs:
	pydocmd simple transporthours.main++ transporthours.openinghoursparser++ > API.md

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf transporthours.egg-info/
