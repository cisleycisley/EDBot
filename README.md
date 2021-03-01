# EDBot - Posts Images to Twitter
EDBot will post a random image of an Enchanted Doll twice daily to twitter account @EnchantedDBot.

tweet $(echo "usb/Galleries/$(ls usb/Galleries/ | sort --random-sort | head -n 1)")
