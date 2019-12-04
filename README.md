# THE
eInk mini MQTT Information Display for Time, Headlines and Environmental Data

Files to setup an run an eink MQTT Information Display

Files are divided into two parts:

Scripts to process data and send to MQTT via cron:

timetomqtt.py - gets the time, converts it to words and publishes to the mqtt topic

rsstomqtt.py - fetches an rss news feed, reads the latest headline and publishes to the mqtt topic

Main script to run the eink display and show mqtt feeds:
