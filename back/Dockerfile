FROM --platform=linux/amd64 python:3.9-slim
WORKDIR /code
COPY ./requirements.txt requirements.txt
RUN pip install --user --no-cache-dir --upgrade -r requirements.txt
COPY . .
WORKDIR /code/db
RUN pip install prisma && prisma generate
WORKDIR /code
EXPOSE 80
CMD python -m uvicorn main:app --host 0.0.0.0 --port 8000