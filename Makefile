# Makefile for demo project

SPEC_FILE=build.spec

all:
	pip3 install -r requirements.txt
	pyinstaller --clean --workpath temp $(SPEC_FILE)

clean:
	rm -rf temp
	rm -rf dist

# END Makefile