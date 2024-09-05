FROM alpine:latest

RUN apk add --no-cache python3 py3-pip

WORKDIR /app

COPY requirements.txt ./
RUN pip install pip --upgrade --break-system-packages
RUN pip install --no-cache-dir -r requirements.txt --break-system-packages

COPY . .

CMD [ "python", "bot.py" ]
