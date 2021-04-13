SHELL := /bin/bash

all:
	@echo 'Makefile for chicken boilerplate'
		
init:
	pip3 install -U pip
	pip3 install django

format:
	@echo 'Formatting...'

lint:
	@echo 'Checking lint...'	

test:
	@echo 'Testing...'

