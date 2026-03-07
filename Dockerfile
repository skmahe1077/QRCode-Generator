FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN pip install --no-cache-dir .

ENV RUNNING_IN_DOCKER=1

EXPOSE 3000

CMD ["qrcodegenerator", "start", "--port", "3000"]
