# OKTOBERFEST FESTZELT SERVICE 🍻

Ever wanted to visit the famous Munich oktoberfest and get your very own table for you/friends/company?  
Well, most of those tables never go public and Oktoberfest is looking "sold out" all the time.
With this service, you can get instant notifications, in the rare situations when vacancies appear.
Delivered directly to telegram.

<hr />
<p align="center">
    <a href="#BUILD">Build</a> • 
    <a href="#RUNNING">Running</a> • 
    <a href="#BOT CONTROL">Bot Control</a> • 
    <a href="#CUSTOMIZATION">Customization</a>
</p>
<hr />

## SETUP  

1. **Create a Telegram Bot**  
You need to create a Telegram Bot, so your first step would be to talk to Botfather.
A detailed manual can be found here:   
[Create a telegram bot](https://core.telegram.org/bots#6-botfather)  
The token created by Botfather is a string like `123456789:ABCDEFGHIJKLMNOPQRSTUVWXYZ` that is required to authorize the bot and send requests to the Bot API.

2. **Start a chat with your Bot**  
You also need a **chat_id**, where vacancies should be delivered by the bot. The `commands` below can help you find the id:
```sh
BOT_TOKEN=123456789:ABCDEFGHIJKLMNOPQRSTUVWXYZ

# Start a Chat with Bot for private communication
# Launch the following command after that:
curl -s https://api.telegram.org/bot$BOT_TOKEN/getUpdates \
| python3 -c "import sys, json; print(str(json.load(sys.stdin)['result'][0]['message']['from']['id']))"

# As an alternative, you can also add the bot to a group channel
# Launch the following command after that:
curl -s https://api.telegram.org/bot$BOT_TOKEN/getUpdates \
| python3 -c "import sys, json; print(str(json.load(sys.stdin)['result'][0]['message']['chat']['id']))"
```

The response is a **chat_id**, group chats start with a `-`. You are ready to go!  

## BUILD

```sh
docker build -f dockerfile -t festzelt-service .
```

## RUNNING

Start the bot and watch vacancies.  

```sh
docker run \
    -it \
    -e TELEGRAM_TOKEN=123456789:ABCDEFGHIJKLMNOPQRSTUVWXYZ \
    -e TELEGRAM_CHANNEL=-987654321 \
    -v festzelt-service:/app/data \
    --name festzelt-service festzelt-service
```
The Bot is a 9-5 worker, Mo-Fr. This is usually the time when staff updates vacancies. Change the cron scheduler job if you like other business hours.

## BOT CONTROL

There are some build in commands in the bot to make it easier to control the service.
Following commands exit:
```
/start  - Main Menu, have a look at the Seatmap
/log    - Status of last vacancy lookup
/stop   - Stops the Service
```

## CUSTOMIZATION
By default, the Bot will look for `Mittag` and `Nachmittag` vacancies on all days of the week.  
This can be changed by by using comma seperated lists when launching the service.

```sh
-e DESIRED_TIMES=Nachmittag
-e DESIRED_DAYS=Montag, Dienstag, Sonntag
```

Currently the following Tents are supported:  
[Schützenzelt](https://www.schuetzenfestzelt.com/)  
[Schottenhamel Festhalle](https://festhalle-schottenhamel.de/)  

Always use the official reservations sites for booking!  
  
Happy 🍺
