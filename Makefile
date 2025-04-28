PYTHON=python

install:
	pip install -r requirements.txt

local-run: 
	uvicorn app.main:app --reload 

test: 
	$(PYTHON) -m pytest

docker-build:
	docker build -t receipt-processor .

docker-run: 
	docker run -d -p 8000:8000 receipt-processor

docker-logs:
	docker logs -f $(shell docker ps -q --filter ancestor=receipt-processor)

