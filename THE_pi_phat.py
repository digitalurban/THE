
import textwrap
import paho.mqtt.client as paho
from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne

#MQTT Details
paho = paho.Client()
# Settings for connection
host = "your mqtt server" #  address of MQTT server
topic= "eink/messages" # topic to subscribe to  - in our case eink/home
port = 1883  # mqtt port  - normally 1883
username = "username"  # username if required
password = "password"  # password if required






def on_connect(mosq, obj, rc):
    print("connect rc: "+str(rc))
    

def on_message(mosq, obj, msg):
# Set up Screen


    inky_display = InkyPHAT("red")
    inky_display.set_border(inky_display.WHITE)
    img = Image.open("/home/pi/scripts/resources/empty-backdrop.png") # displays an empty background
    draw = ImageDraw.Draw(img)

# Set MQTT Message 
    
    message = str(msg.payload.decode('UTF-8'))

# Set Font etc and Refresh 
    if "The Time" in message:
        font = ImageFont.truetype("/home/pi/scripts/resources/hm.ttf", 25) # any ttf font can be used
        fonttop = ImageFont.truetype("/home/pi/scripts/resources/hm.ttf", 25) # any ttf font can be used
        wrapped = textwrap.wrap(message, width=15)

        if (len(wrapped) >= 1):
            # Status Line 1
            status_one = wrapped[0]
            w, h = font.getsize(status_one)
            # Center the text and align it with the name strip
            x = (inky_display.WIDTH / 2) - (w / 2)
            y = 10 - (h / 2)
            draw.text((0, 0), status_one, inky_display.RED, fonttop, align="left")

        if (len(wrapped) >= 2):
            # Status Line 2
            status_two = wrapped[1]
            w, h = font.getsize(status_two)
            # Center the text and align it with the name strip
            x = (inky_display.WIDTH / 2) - (w / 2)
            y = 35 - (h / 2)
            draw.text((0, 25), status_two, inky_display.BLACK, font, align="left")

        if (len(wrapped) >= 3):
            # Status Line 3
            status_three = wrapped[2]
            w, h = font.getsize(status_one)
            # Center the text and align it with the name strip
            x = (inky_display.WIDTH / 2) - (w / 2)
            y = 60 - (h / 2)
            draw.text((0, 50), status_three, inky_display.BLACK, font, align="left")

        if (len(wrapped) >= 4):
            # Status Line 4
            status_four = wrapped[3]
            w, h = font.getsize(status_one)
            # Center the text and align it with the name strip
            x = (inky_display.WIDTH / 2) - (w / 2)
            y = 85 - (h / 2)
            draw.text((0, 75), status_four, inky_display.BLACK, font, align="left")

    else:

        font = ImageFont.truetype("/home/pi/scripts/resources/hm.ttf", 14) # smaller font for longer text
        fonttop = ImageFont.truetype("/home/pi/scripts/resources/hm.ttf", 14) # smaller font for longer text
        wrapped = textwrap.wrap(message, width=29)

        if(len(wrapped) >= 1):
            # Status Line 1
            status_one = wrapped[0]
            w, h = font.getsize(status_one)
            # Center the text and align it with the name strip
            x = (inky_display.WIDTH / 2) - (w / 2)
            y = 10 - (h / 2)
            draw.text((0, 0), status_one, inky_display.RED, fonttop, align="left")


        if(len(wrapped) >= 2):
            # Status Line 2
            status_two = wrapped[1]
            w, h = font.getsize(status_two)
            # Center the text and align it with the name strip
            x = (inky_display.WIDTH / 2) - (w / 2)
            y = 35 - (h / 2)
            draw.text((0, 20), status_two, inky_display.BLACK, font, align="left")

        if(len(wrapped) >= 3):
            # Status Line 3
            status_three = wrapped[2]
            w, h = font.getsize(status_one)
            # Center the text and align it with the name strip
            x = (inky_display.WIDTH / 2) - (w / 2)
            y = 60 - (h / 2)
            draw.text((0, 40), status_three, inky_display.BLACK, font, align="left")

        if(len(wrapped) >= 4):
            # Status Line 4
            status_four = wrapped[3]
            w, h = font.getsize(status_one)
            # Center the text and align it with the name strip
            x = (inky_display.WIDTH / 2) - (w / 2)
            y = 85 - (h / 2)
            draw.text((0, 60), status_four, inky_display.BLACK, font, align="left")

        if(len(wrapped) >= 5):
            # Status Line 5
            status_five = wrapped[4]
            w, h = font.getsize(status_one)
            # Center the text and align it with the name strip
            x = (inky_display.WIDTH / 2) - (w / 2)
            y = 85 - (h / 2)
            draw.text((0, 80), status_five, inky_display.BLACK, font, align="left")


    flipped = img.rotate(180)
    inky_display.set_image(flipped)
    inky_display.show()
    print (message)




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


