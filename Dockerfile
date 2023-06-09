# syntax=docker/dockerfile:1
   
FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install -r ./requirements.txt
EXPOSE 9100
ENV TRAIN_DATA_PATH data/raw
ENV RES_DATA_PATH data/processed
ENV PARAMS_DIR params
ENV LOG_FILE logs/logs.log
ENV MODE prod
CMD ["python", "./src/data/process_data.py", "process"]
CMD ["python", "./src/models/process_model.py", "process"]
CMD ["python", "./src/server/main.py"]