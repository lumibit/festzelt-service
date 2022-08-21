# OKTOBERFEST FESTZELT SERVICE 🍻

Ever wanted to visit the famous Munich oktoberfest and get your very own table for you/friends/company?  
Well, most of those tables never go public and Oktoberfest is looking "sold out" all the time.
With this service, you can get instant notifications when the tent staff releases new availabilities.  
This happens normally between 11-15 CET on working days.  
Delivered directly to telegram.  

<hr />
<p align="center">
    <a href="#SETUP">Setup</a> • 
    <a href="#DEPLOYMENT">Deployment</a> • 
    <a href="#CUSTOMIZATION">Customization</a> • 
    <a href="#DEBUGGING">Debugging</a>
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

## DEPLOYMENT

`terraform apply` will deploy this bot to your AWS Cloudroom.  

Setup your AWS Provider and the necessary variables before.  

```terraform
provider "aws" {
  region  = "eu-central-1"
  profile = "YOUR_AWS_PROFILE"
}
```

> Docker must be up and running as well while deploying

## CUSTOMIZATION
By default, the Bot will look for `Mittag` and `Nachmittag` vacancies on all days of the week.  
This can be changed using the terraform variables `desired_times` and `desired_days`.  

```terraform
desired_days     = "Montag, Dienstag, Mittwoch, Donnerstag, Freitag, Samstag, Sonntag"
desired_times    = "Nachmittag"
```

Currently the following Tents are supported:  
[Schützenzelt](https://www.schuetzenfestzelt.com/)  
[Schottenhamel Festhalle](https://festhalle-schottenhamel.de/)  
[Hacker Zelt](https://hacker-festzelt.de/)  

Always use the official reservations sites for booking!  

## DEBUGGING

### SOURCE CODE

Setup the necessary environment variables

```json
  "env": {
      "PYTHON_LOGLEVEL": "DEBUG",
      "TELEGRAM_TOKEN": "YOUR_TELEGRAM_TOKEN",
      "TELEGRAM_CHANNEL": "-12345678",
      "SESSION_STORAGE": "data/vacancies.json",
      "BUCKET_NAME": "wiesn-zelt-crawler",
      "DESIRED_TIMES": "Mittag, Nachmittag",
      "DESIRED_DAYS": "Montag, Dienstag",
      "DEBUG": true
  }
```

### AWS

Build the lambda-layer locally.

```sh
docker build -f Dockerfile -t lambdalayer . 
```

> If you are using `aws sso login` remember to call `aws sts get-caller-identity` after login for credential population.
  
Happy 🍺
