# Read Client Raw, Remap to Conditions and send to MQTT for LED Matrix


import paho.mqtt.client as paho
import time
import datetime


# Schedule
    
# MQTT


#MQTT Details
paho = paho.Client()
# Settings for connection
host = "your mqtt server" # #  address of MQTT server
topic= "wd/#"  # topic to read the clientraw data from - in our case wd
port = 1883 # mqtt port  - normally 1883
username  = "username" # username if required
password = "password" # password if required



# Callbacks - Needed to receive messages


def on_connect(mosq, obj, rc):
    print("connect rc: "+str(rc))
    

def on_message(mosq, obj, msg):

    contents = str(msg.payload)
    print (contents)



    # Read MQTT Feed

    # Split Based on Spaces

    data = contents.split()

    # Get Conditions Code from ClientRaw

    conditions = (data[48])

    # Get Temperature Code from ClientRaw

    temp = str(data[4])

    # Get Temperature Trend and Convert Code from ClientRaw

    temptrend = int(data[143])

    if temptrend == 1:
        temptrend = "& Rising"
    if temptrend == -1:
        temptrend = "& Falling"

    # Get Pressure Code from ClientRaw

    press = str(data[6])


    # Get Pressure Trend and Convert Code from ClientRaw

    presstrend = float(data[50])

    if presstrend > +0.1:
        presstrend = "& Rising"
    elif presstrend < -0.1:
        presstrend = "& Falling"
    else: presstrend = "& Steady"

    # Get Rain Code from ClientRaw

    rainday = str(data[7])


    # Get Rain Rate Code from ClientRaw - to Trigger Show Rain on MQTT Feed

    rainrate = float(data[10])

    # Get Wind Gust (Av Last 10 Min) Code from ClientRaw

    wind = str(data[158])

    # Get Wind Direction and Convert Code to Readable Direction from ClientRaw

    windir = int(data[3])

    if windir >=  11.25 and windir <  33.75:
        windir = "North North East"
    elif windir >=  33.75 and windir <  56.25:
        windir = "North East"
    elif windir >=  56.25 and windir <  78.75:
        windir = "East North East"
    elif windir >=  78.75 and windir < 101.25:
        windir =East
    elif windir >= 101.25 and windir < 123.75:
        windir = "East South East"
    elif windir >= 123.75 and windir < 146.25: 
        windir = "South East"
    elif windir >= 146.25 and windir < 168.75:
        windr = "South South East"
    elif windir >= 168.75 and windir < 191.25:
        windir = "Southerly"
    elif windir >= 191.25 and windir < 213.75:
        windir = "South South West"
    elif windir >= 213.75 and windir < 236.25:
        windir = "South West"
    elif windir >= 236.25 and windir < 258.75:
        windir = "West South West"
    elif windir >= 258.75 and windir < 281.25:
        windir = "Westerly"
    elif windir >= 281.25 and windir < 303.75:
        windir = "West North West"
    elif windir >= 303.75 and windir < 326.25:
        windir = "North West"
    elif windir >= 326.25 and windir < 348.75:
        windir = "North North West"
    else: windir = "Northerly"


    # Remap Conditions Code to Text

    # Sunny

    if conditions == '0':
        conditions = 'Sunny'

    # Mainly cloudy
        
    if conditions == '18':
        conditions = 'Dry, Mainly Cloudy'

    # Partly cloudy
        
    if conditions == '19':
        conditions = 'Partly Cloudy'

    if conditions == '2':
        conditions = 'Partly Cloudy'

    if conditions == '3':
        conditions = 'Partly Cloudy'

    # Sunny Spells
        
    if conditions == '5':
        conditions = 'Sunny Spells'


    # Light Rain

    if conditions == '21':
        conditions = 'Light Rain'
        
    if conditions == '22':
        conditions = 'Light Rain'
        

    if conditions == '23':
        conditions = 'Light Rain'

    # Night Light Rain

    if conditions == '15':
        conditions = 'Light Rain'

    # Rain

    if conditions == '20':
        conditions = 'Rain'

    # Night Rain

    if conditions == '14':
        conditions = 'Night Time: Rain'

    # Stopped raining - Day or Night

    if conditions == '34':
        conditions = 'Stopped Raining'

    # Night Clear
        
    if conditions == '1':
        conditions = 'Night Time, Clear'

    # Night Fog
        
    if conditions == '11':
        conditions = 'Night Time, Mist/Fog'

    # Sleet

    if conditions == '16':
        conditions = 'Sleet'
        
    # Print and Publish Output


    output_string = "The Weather is " + conditions + ", " + temp + " Degrees Centigrade " + temptrend + "," + " " + "Pressure: " + press + " Mb " + presstrend + ", Wind "+ windir + " " + wind + " Mph" 

    output_string_rain = "The Weather is " + conditions + ", " + rainday + " mm" + ", " + temp + " Degrees Centigrade " + temptrend + "," + " " + "Pressure: " + press + " Mb " + presstrend + ", Wind "+ windir + " " + wind + " Mph" 


    #Get Time
    currentDT = datetime.datetime.now()
    #Print Time
    print ("Publishing at: ", currentDT.strftime("%I:%M:%S %p"))
    #Print Output
    print (output_string)

    # Send to MQTT
        
    print("Publishing message to topic")

    #Publish to MQTT - Include Rain if Rain Rate Hour is > 0mm
    if rainrate > 0:

       paho.publish("eink/home", output_string_rain)  # topic to publish the conditions to ie eink/messages

    else: paho.publish("eink/home", output_string)  # topic to publish the conditions to ie eink/messages

  
# Following Sections MQTT to Run Defs and Keep Live  

def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed OK")
 

# Set callbacks
paho.on_message = on_message
paho.on_connect = on_connect
paho.on_subscribe = on_subscribe
 
# Connect and subscribe
print("Connecting to " +host +"/" +topic)
paho.connect(host, port, 60)
paho.subscribe(topic, 0)

 
# Wait forever, receiving messages
rc = 0
while rc == 0:
    rc = paho.loop()
print("rc: "+str(rc))
print (msg.payload)




