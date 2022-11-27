install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
    
format:
	black *.py mylibrary/*.py

all: install format
