# Python Groundstation
**Project Charter:** lol

## Description
*This project is an MVP groundstation software package for Anduril 2*
*The package uses docker to run both direwolf and a python script*
*direwolf is configured to log decoded packets to aprs.log*
*the python script takes a COM port as an argument and logs serial data from the COM port to Anduril2Telemetry.txt*

## Setup Guide
*[Fill out if applicable]*
clone the repo
install docker: https://docs.docker.com/get-started/get-docker/
run: `(sudo) docker-compose build`
make sure the RTL-SDR is inserted
next run: `docker-compose up`
open a second terminal and run: ` docker exec -it aprs_direwolf bash `
finally: `python3 src/main.py`

*now the direwolf service is running in the background and you have access to the python app's cli interface