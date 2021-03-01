#!/bin/sh

tweet $(echo "usb/Galleries/$(ls usb/Galleries/ | sort --random-sort | head -n 1)")
