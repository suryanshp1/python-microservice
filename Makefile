install:
	# install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	# format code
	#black *.py mylib/*.py
	black .
lint:
	# flake8 or pylint
	pylint --disable=R,C *.py mylib/*.py
test:
	# test
	python -m pytest -vv --cov=mylib --cov=main test_logic.py test_main.py
build:
	# build container
	docker build -t deploy-fastapi .
run:
	# run docker
	# docker run -p 127.0.0.1:8080:8080 2790abac1fca
deploy:
	# deploy
all: install lint test build deploy