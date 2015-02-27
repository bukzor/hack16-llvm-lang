all:
	python hello.py > hello.ll
	llc hello.ll
	clang hello.s -o hello
	./hello
