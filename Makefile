SHELL := /bin/bash
.DEFAULT_GOAL := help

CURRENT_UID := $(shell id -u)

DOCKER_COMPOSE := docker-compose build --parallel --quiet && docker-compose run --user="$(CURRENT_UID)"

FLAKE8 := $(DOCKER_COMPOSE) flake8
SOLVER := $(DOCKER_COMPOSE) solver
TEST := $(DOCKER_COMPOSE) test

##@ Entry Points
.PHONY: lint ## Run flake8 docker-compose service
lint: _clean
	echo "Running flake8"
	$(FLAKE8) sudoku_solver

.PHONY: test
test: ## Run tests
	echo "Running tests"
	$(TEST) pytest -v --disable-warnings -r sudoku_solver

.PHONY: solver ## Run solver application
solver: _clean
	$(SOLVER)

##@ Helpers
.PHONY: flake8 ## Shortcut to lint entrypoint
flake8: lint

.PHONY: _clean
_clean: ## Remove all unused files
	docker-compose down --rmi all 2>/dev/null

##@ Misc
.PHONY: help ## Display this help
help:
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'
