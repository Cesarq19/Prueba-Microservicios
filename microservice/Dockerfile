FROM tiangolo/uvicorn-gunicorn-fastapi

COPY ./microservice /app/microservice

RUN pip install --no-cache-dir -r /app/microservice/requirements.txt

EXPOSE 8000

CMD [ "uvicorn", "microservice.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload" ]
