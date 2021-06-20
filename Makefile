VENV := ./venv
BIN := ${VENV}/bin


venv: backend/requirements.txt
	python3 -m venv ${VENV}
	${BIN}/pip install -r backend/requirements.txt
	touch ${VENV}


run: venv
	${BIN}/uvicorn api.main:app --reload

max_perf: venv
	${BIN}/pip install gunicorn
	${BIN}/gunicorn api.main:app -w 8 -k uvicorn.workers.UvicornWorker

${BIN}/tox: venv
	${BIN}/pip install tox

test: ${BIN}/tox
	${BIN}/tox
