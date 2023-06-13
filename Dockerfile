# syntax=docker/dockerfile:1
   
FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install -r ./requirements.txt
ENV TRAIN_DATA_PATH data/raw
ENV RES_DATA_PATH data/processed
ENV PARAMS_DIR params
ENV LOG_FILE logs/logs.log
ENV MODE prod
EXPOSE 9100
CMD ["chmod +x start.sh", "./start.sh"]