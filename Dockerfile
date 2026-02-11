FROM python:3.11-slim
WORKDIR /app
COPY  backend.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 5001
CMD ["python" , "backend.py"]