# Python3 program to convert  
# time into words
import paho.mqtt.client as mqtt    #Import MQTT
from time import gmtime, strftime  #Import time


# MQTT

print("creating new instance")
client = mqtt.Client("P1") #  create new instance
print("connecting to broker")
client.username_pw_set("username", "password") # user name / password if required
client.connect("add your mqtt details", 1883) #  address and port of MQTT server



h = int(strftime("%H", gmtime()))
m = int(strftime("%M", gmtime()))
print(h, m)

'2009-01-05 22:14:39'


# Print Time in words. 

nums = ["zero", "One", "Two", "Three", "Four", 
        "Five", "Six", "Seven", "Eight", "Nine", 
        "Ten", "Eleven", "Twelve", "Thirteen", 
        "Fourteen", "Fifteen", "Sixteen",  
        "Seventeen", "Eighteen", "Nineteen",  
        "Twenty", "Twenty One", "Twenty Two",  
        "Twenty Three", "Twenty Four",  
        "Twenty Five", "Twenty Six", "Twenty Seven", 
        "Twenty Eight", "Twenty Nine"];

hours = ["zero","One", "Two", "Three", "Four", 
        "Five", "Six", "Seven", "Eight", "Nine", 
        "Ten", "Eleven", "Twelve", "One", "Two", "Three", "Four", 
        "Five", "Six", "Seven", "Eight", "Nine", 
        "Ten", "Eleven", "Twelve"]


if (m == 0):
    time =  "The Time is " + hours[h] + " o' Clock"; 

elif (m == 1): 
    time = "The Time is "+ "One Minute Past " + hours[h];

elif (m == 59): 
    time = "The Time is " + "One Minute to " + hours[(h % 12) + 1]; 

elif (m == 15): 
    time = "The Time is " + "a Quarter Past " + hours[h]; 

elif (m == 30): 
    time = "The Time is " + "Half Past " + hours[h];

elif (m == 45):

    time = "The Time is " + "a Quarter to " + (hours[(h % 12) + 1]); 

elif (m <= 30): 
    time = "The Time is " +nums[m] + " Minutes Past " + hours[h]; 

elif (m > 30): 
    time = "The Time is " + nums[60 - m] + " Minutes to " + hours[(h)+1];

timeprint = time


print(timeprint)


# Send to MQTT
    
print("Publishing message to topic")


client.publish("THE/messages", str(time))  # topic to publish the time ie eink/messages
  
# This code is adapted from the original script at
# https://sukhbinder.wordpress.com/2013/12/29/time-in-words-with-python/
# by Princi Singh 
