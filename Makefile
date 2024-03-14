VENV := .venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip
SRC := $(wildcard src/*.py)

# Default target
.PHONY: all
all: setup ft_ality

# Setup Python environment and install dependencies
setup: $(VENV)/bin/activate

$(VENV)/bin/activate: requirements.txt
	@test -d $(VENV) || python3 -m venv $(VENV)
	@$(PIP) install -r requirements.txt
	@touch $(VENV)/bin/activate

# Create ft_ality executable
ft_ality: $(SRC) requirements.txt
	@echo "Creating or updating ft_ality executable..."
	@echo '#!/bin/bash' > ft_ality
	@echo 'source $(VENV)/bin/activate' >> ft_ality
	@echo '$(PYTHON) src/main.py "$$@"' >> ft_ality
	@echo 'deactivate' >> ft_ality
	@chmod +x ft_ality

clean:
	@rm -rf $(VENV)
	@find . -type f -name '*.pyc' -delete
	@find . -type d -name '__pycache__' -delete
	@rm -f ft_ality

.PHONY: setup clean
