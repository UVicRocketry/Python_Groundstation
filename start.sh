#!/bin/bash
rtl_fm -f 144.39M -s 22050 - | direwolf -r 22050 -D 1 - > /app/logs/aprs.log
