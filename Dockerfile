FROM ultralytics/ultralytics:latest

ENV PYTHONUNBUFFERED True

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["streamlit", "run", "--server.port", "8080", "--server.enableCORS", "false", "app.py", "--server.fileWatcherType=none"]
