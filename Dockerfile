FROM 		python:3.8-alpine

ENV         PYTHONUNBUFFERED=1

WORKDIR		/home

COPY		./requirements.txt .

RUN 		pip install -r requirements.txt \
			&& adduser --disabled-password --no-create-home doe

COPY 		* .

USER 		doe

EXPOSE		8000

CMD 		["uvicorn", "main:app", "--port", "8000", "--host", "0.0.0.0"]
