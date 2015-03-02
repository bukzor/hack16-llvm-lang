.PHONY: all
all: CI

.PHONY: CI
CI: lint test

.PHONY: lint
lint:
	pre-commit run --all

.PHONY: test tests
test tests:
	./.travis/test.sh $(ARGS)

.PHONY: tox
tox:
	tox -e lint,test

.PHONY: clean
clean:
	rm -rf .tox
	find -name '*.pyc' -print0 | xargs -0 -r -P4 rm

.PHONY: build
build:
	emcc hello.c -O3 -s EXPORTED_FUNCTIONS="['_main', '_eval']" -s NO_EXIT_RUNTIME=True -o chrome-extension/scripts/hello.js
