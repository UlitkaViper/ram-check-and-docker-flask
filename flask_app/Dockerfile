
FROM python:3.10-alpine
COPY ./flask_app/requirements.txt /app/requirements.txt
COPY ./.env /app/.env
WORKDIR /app
RUN pip install -r requirements.txt
COPY ./flask_app /app
ENTRYPOINT ["python"]
CMD ["app.py"]