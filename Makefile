SHELL := /bin/bash

all:
	@echo 'Makefile for chicken boilerplate'
		
init:
	python3 -m pip install --upgrade pip
	python3 -m venv default
	. default/bin/activate
	pip3 install -U pip
	pip3 install django

activate:
	(\
	source default/bin/activate; \
    	)	

format:
	@echo 'Formatting...'

lint:
	@echo 'Checking lint...'	

test:
	@echo 'Testing...'

