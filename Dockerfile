FROM python:3
COPY . /app
WORKDIR /app
ENV jenkins_sys Docker
RUN pip install -r requirements.txt
CMD ["python","s.py"]