


import forecastio
import paho.mqtt.client as mqtt

# MQTT

print("creating new instance")
client = mqtt.Client("P1") # create new instance
print("connecting to broker")
client.connect("yourmqttserver", 1883) #  address and port of MQTT server
username  = "username" # username if required
password = "password" # password if required

# Dark Sky Details
api_key = "your api key"
lat = your lat
lng = your long

forecast = forecastio.load_forecast(api_key, lat, lng)

# Get Current Conditions and Forecast

current =forecast.currently()
hour =forecast.hourly()
temp = str(current.temperature)
pressure = str(current.pressure)
windir = (current.windBearing)
wind = str(current.windGust)
forecast = str(hour.summary)

# Convert the Wind Bearing to Text

if windir >= 11.25 and windir < 33.75 :
    windir = "North North East"
elif windir >= 33.75 and windir < 56.25 :
    windir = "North East"
elif windir >= 56.25 and windir < 78.75 :
    windir = "East North East"
elif windir >= 78.75 and windir < 101.25 :
    windir = East
elif windir >= 101.25 and windir < 123.75 :
    windir = "East South East"
elif windir >= 123.75 and windir < 146.25 :
    windir = "South East"
elif windir >= 146.25 and windir < 168.75 :
    windr = "South South East"
elif windir >= 168.75 and windir < 191.25 :
    windir = "Southerly"
elif windir >= 191.25 and windir < 213.75 :
    windir = "South South West"
elif windir >= 213.75 and windir < 236.25 :
    windir = "South West"
elif windir >= 236.25 and windir < 258.75 :
    windir = "West South West"
elif windir >= 258.75 and windir < 281.25 :
    windir = "Westerly"
elif windir >= 281.25 and windir < 303.75 :
    windir = "West North West"
elif windir >= 303.75 and windir < 326.25 :
    windir = "North West"
elif windir >= 326.25 and windir < 348.75 :
    windir = "North North West"
else :
    windir = "Northerly"


# Create the Output for THE

output = "The Weather is " + current.summary + ", " + temp + " Degrees Centigrade," + " Pressure: " + pressure + " Mb," + " Wind " + windir + " " + wind + " Mph, " + forecast
print (output)

print ("Publishing message to topic")

# Publish to MQTT

client.publish("eink/home", output)  # topic to publish to
