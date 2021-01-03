#!/bin/bash
DATE=$(date +"%Y%m%d-%H%M%S")
raspistill -o /home/pi/Documents/timelapse/pictures_cron/$DATE.jpg


