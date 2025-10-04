all: build
	@./main.bin

build:
	gcc -g -O0 main.c -o main.bin
