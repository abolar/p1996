FROM python:3
COPY . /app
WORKDIR /app
ENV sys BUILD
RUN pip install -r requirements.txt
CMD ["python","s.py"]