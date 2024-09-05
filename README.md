# Pycord

Bot en Python para Discord

## Cómo ejecutar en Docker

- Construir imágen del Bot
Para construir una imágen usa:
```
docker build . -t pycord
```

- Ejecuar Imágen del Bot
Para ejecutar la imágen creada del bot, usa:
```
docker run -d --restart unless-stopped --name=pycord --env TOKEN=TOKEN pycord:latest
```
En la variable de entorno `--env TOKEN=` ingresa el token que te proporciona la página `https://discord.com/developersapplications` para poder ejecutar el bot en la aplicación creada.

- Verificar funcionamiento del Bot
Para verificar el correcto funcionamiento del Bot usa:
```
docker ps -a
```
para ver los bot que se están ejecuatndo en ese momento.

Usa `docker logs pycord -f` para ver los Logs del Bot.
