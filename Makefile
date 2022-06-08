POETRY_BIN 		:= $(shell which poetry)
PIPX_BIN 		:= $(shell which pipx)
PYTHON_BIN		:= $(shell which python)
PACKAGE_NAME    := vnu
PACKAGE_VERSION := $(shell $(POETRY_BIN) version | cut -d' ' -f2)
DIST_PATH       := dist
PACKAGE_DIST    := $(DIST_PATH)/$(PACKAGE_NAME)-$(PACKAGE_VERSION).tar.gz

clean:
	rm -rf build $(DIST_PATH)
	find . -type d -name '*.egg-info' -exec rm -rf {} +
	find . -type d -name '__pycache__' -exec rm -rf {} +
	find . -type d -name '*pytest_cache*' -exec rm -rf {} +
	find . -type f -name "*.py[co]" -exec rm -rf {} +

install: pyproject.toml
	$(POETRY_BIN) install

pipx-install: $(PACKAGE_DIST)
	$(PIPX_BIN) install $<

uninstall: clean
	$(PIPX_BIN) uninstall $(PACKAGE_NAME)

build:
	$(POETRY_BIN) build -f sdist

setup: clean install build pipx-install
