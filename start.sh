#!/bin/bash
while true; do
  rtl_fm -f 144.39M -s 22050 - | direwolf -r 22050 -D 1 - > /app/logs/aprs.log
  echo "Direwolf exited. Ensure RTL SDR connected. Retrying in 5s"
  sleep 5
done