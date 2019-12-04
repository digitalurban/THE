import feedparser
import paho.mqtt.client as mqtt

#Get News Feed - in this case Sky News

NewsFeed = feedparser.parse("http://feeds.skynews.com/feeds/rss/home.xml") # edit to add any news feed

entry = NewsFeed.entries[0] # get the latest (first) entry

print (entry.summary)

# MQTT

print("creating new instance")
client = mqtt.Client("P1") # create new instance
print("connecting to broker")
client.username_pw_set("username", "password") # user name / password if required
client.connect("add your mqtt details", 1883) #  address and port of MQTT server


# Send to MQTT
    
print("Publishing message to topic")


client.publish("yourtopic/topic", str(time))  # topic to publish the time ie eink/messages


