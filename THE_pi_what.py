
import textwrap
import paho.mqtt.client as paho
from inky import InkyWHAT
from PIL import Image, ImageFont, ImageDraw
import sys


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

    
        
# Set MQTT Message 
    
    message = str(msg.payload.decode('UTF-8'))

    print(message)

# Set Font etc and Refresh 


    
    inky_display = InkyWHAT("red")
    inky_display.set_border(inky_display.WHITE)
    img = Image.open("/home/pi/scripts/resources/whatbackground.png") #adds a red line at the bottom
    draw = ImageDraw.Draw(img)

    
    # Display the completed canvas on Inky wHAT


    if 'Weather' in message:
        fonttop = ImageFont.truetype("/home/pi/scripts/resources/hm.ttf", 30) # any ttf font can be used
        font = ImageFont.truetype("/home/pi/scripts/resources/hm.ttf", 30) # any ttf font can be used
        wrapped = textwrap.wrap(message, width=24)

        if(len(wrapped) >= 1):
            # Status Line 1
            status_one = wrapped[0]
            w, h = font.getsize(status_one)
            # Center the text and align it with the name strip
            x = (inky_display.WIDTH / 2) - (w / 2)
            y = 10 - (h / 2)
            draw.text((15, 30), status_one, inky_display.RED, fonttop, align="left")


        if(len(wrapped) >= 2):
            # Status Line 2
            status_two = wrapped[1]
            w, h = font.getsize(status_one)
            # Center the text and align it with the name strip
            x = (inky_display.WIDTH / 2) - (w / 2)
            y = 35 - (h / 2)
            draw.text((15, 70), status_two, inky_display.BLACK, font, align="left")

        if(len(wrapped) >= 3):
            # Status Line 3
            status_three = wrapped[2]
            w, h = font.getsize(status_one)
            # Center the text and align it with the name strip
            x = (inky_display.WIDTH / 2) - (w / 2)
            y = 60 - (h / 2)
            draw.text((15, 110), status_three, inky_display.BLACK, font, align="left")
            
        if(len(wrapped) >= 4):
            # Status Line 4
            status_four = wrapped[3]
            w, h = font.getsize(status_one)
            # Center the text and align it with the name strip
            x = (inky_display.WIDTH / 2) - (w / 2)
            y = 85 - (h / 2)
            draw.text((15, 150), status_four, inky_display.BLACK, font, align="left")
            
        if(len(wrapped) >= 5):
            # Status Line 5
            status_five = wrapped[4]
            w, h = font.getsize(status_one)
            # Center the text and align it with the name strip
            x = (inky_display.WIDTH / 2) - (w / 2)
            y = 85 - (h / 2)
            draw.text((15, 190), status_five, inky_display.BLACK, font, align="left")

        if(len(wrapped) >= 6):
            # Status Line 5
            status_six = wrapped[5]
            w, h = font.getsize(status_one)
            # Center the text and align it with the name strip
            x = (inky_display.WIDTH / 2) - (w / 2)
            y = 85 - (h / 2)
            draw.text((15, 230), status_six, inky_display.BLACK, font, align="left")

        

    elif 'Time' in message:
        fonttop = ImageFont.truetype("/home/pi/scripts/resources/hm.ttf", 50) # larger text for time
        font = ImageFont.truetype("/home/pi/scripts/resources/hm.ttf", 50) # larger text for time
        wrapped = textwrap.wrap(message, width=14)
        
        if(len(wrapped) >= 1):
        # Status Line 1
            status_one = wrapped[0]
            w, h = font.getsize(status_one)
            # Center the text and align it with the name strip
            x = (inky_display.WIDTH / 2) - (w / 2)
            y = 10 - (h / 2)
            draw.text((15, 40), status_one, inky_display.RED, fonttop, align="left")


        if(len(wrapped) >= 2):
            # Status Line 2
            status_two = wrapped[1]
            w, h = font.getsize(status_two)
            # Center the text and align it with the name strip
            x = (inky_display.WIDTH / 2) - (w / 2)
            y = 35 - (h / 2)
            draw.text((15, 100), status_two, inky_display.BLACK, font, align="left")

        if(len(wrapped) >= 3):
            # Status Line 3
            status_three = wrapped[2]
            w, h = font.getsize(status_three)
            # Center the text and align it with the name strip
            x = (inky_display.WIDTH / 2) - (w / 2)
            y = 60 - (h / 2)
            draw.text((15, 160), status_three, inky_display.BLACK, font, align="left")
            
        if(len(wrapped) >= 4):
            # Status Line 4
            status_four = wrapped[3]
            w, h = font.getsize(status_four)
            # Center the text and align it with the name strip
            x = (inky_display.WIDTH / 2) - (w / 2)
            y = 85 - (h / 2)
            draw.text((15, 220), status_four, inky_display.BLACK, font, align="left")
            

    else:
        fonttop = ImageFont.truetype("/home/pi/scripts/resources/hm.ttf", 24)
        font = ImageFont.truetype("/home/pi/scripts/resources/hm.ttf", 26)
        wrapped = textwrap.wrap(message, width=27.5)

        if(len(wrapped) >= 1):
            # Status Line 1
            status_one = wrapped[0]
            w, h = font.getsize(status_one)
            # Center the text and align it with the name strip
            x = (inky_display.WIDTH / 2) - (w / 2)
            y = 10 - (h / 2)
            draw.text((15, 10), status_one, inky_display.RED, fonttop, align="left")


        if(len(wrapped) >= 2):
            # Status Line 2
            status_two = wrapped[1]
            w, h = font.getsize(status_two)
            # Center the text and align it with the name strip
            x = (inky_display.WIDTH / 2) - (w / 2)
            y = 35 - (h / 2)
            draw.text((15, 50), status_two, inky_display.BLACK, font, align="left")

        if(len(wrapped) >= 3):
            # Status Line 3
            status_three = wrapped[2]
            w, h = font.getsize(status_three)
            # Center the text and align it with the name strip
            x = (inky_display.WIDTH / 2) - (w / 2)
            y = 60 - (h / 2)
            draw.text((15, 90), status_three, inky_display.BLACK, font, align="left")
            
        if(len(wrapped) >= 4):
            # Status Line 4
            status_four = wrapped[3]
            w, h = font.getsize(status_four)
            # Center the text and align it with the name strip
            x = (inky_display.WIDTH / 2) - (w / 2)
            y = 85 - (h / 2)
            draw.text((15, 130), status_four, inky_display.BLACK, font, align="left")
            
        if(len(wrapped) >= 5):
            # Status Line 5
            status_five = wrapped[4]
            w, h = font.getsize(status_five)
            # Center the text and align it with the name strip
            x = (inky_display.WIDTH / 2) - (w / 2)
            y = 85 - (h / 2)
            draw.text((15, 170), status_five, inky_display.BLACK, font, align="left")

        if(len(wrapped) >= 6):
            # Status Line 5
            status_six = wrapped[5]
            w, h = font.getsize(status_six)
            # Center the text and align it with the name strip
            x = (inky_display.WIDTH / 2) - (w / 2)
            y = 85 - (h / 2)
            draw.text((15, 210), status_six, inky_display.BLACK, font, align="left")

        if(len(wrapped) >= 7):
            # Status Line 5
            status_seven = wrapped[6]
            w, h = font.getsize(status_seven)
            # Center the text and align it with the name strip
            x = (inky_display.WIDTH / 2) - (w / 2)
            y = 85 - (h / 2)
            draw.text((15, 250), status_seven, inky_display.BLACK, font, align="left")    

            # Display the completed canvas on Inky wHAT 

    
    inky_display.set_image(img)
    inky_display.show()
    print (message)





# Following Sections MQTT to Keep Live

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


