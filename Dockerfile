


FROM python:3
COPY . /app
WORKDIR /app
RUN ls
CMD ["python","s.py"]