# EDBot - Posts Images to Twitter
EDBot will post a random image of an Enchanted Doll twice daily to twitter account @EnchantedDBot.

## Setup

1. Clone the repo with `git clone git@github.com:cisleycisley/EDBot.git`
2. Setup pip dependencies `cd EDBot && pip install -r requirements.txt`
3. Copy `env.example` to `.env` and supply your Twitter API Key and API Secret

## Usage

```shell

tweet $(echo "usb/Galleries/$(ls usb/Galleries/ | sort --random-sort | head -n 1)")
```
