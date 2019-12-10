# THE
eInk mini MQTT Information Display for Time, Headlines and Environmental Data

Files to setup an run an eink MQTT Information Display

See https://www.connected-environments.org/making/the/ 

Files are divided into two parts:

Scripts to process data and send to MQTT via cron:

timetomqtt.py - gets the time, converts it to words and publishes to the mqtt topic

rsstomqtt.py - fetches an rss news feed, reads the latest headline and publishes to the mqtt topic

clientrawmqttwd.py - fetches the feed from Weather Display and converts the data into text to publish - if you have your own personal weather station

or

darkskytomqtt.py - fetches the weather from Dark Sky, converts the wind bearing into text and publishes to your MQTT feed

Main script to run the eink display and show mqtt feeds:

Version for the eink PHAT:

the_pi_phat.py

Version for the eink WHAT:

the_pi_what.py

To check - font download, background images
