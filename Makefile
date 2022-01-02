VENV := $(shell pwd)/venv
BIN := ${VENV}/bin


venv: backend/requirements.txt
	python3 -m venv ${VENV}
	${BIN}/pip install -r backend/requirements-dev.txt
	touch ${VENV}


run: venv
	${BIN}/uvicorn api.main:app --reload --reload-dir backend/api --host=0.0.0.0 --port=8009

max_perf: venv
	${BIN}/pip install gunicorn
	${BIN}/gunicorn api.main:app -w 8 -k uvicorn.workers.UvicornWorker

${BIN}/tox: venv
	${BIN}/pip install tox

test: ${BIN}/tox
	${BIN}/tox
