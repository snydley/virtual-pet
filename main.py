from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf
import time
import random

# display code sourced from https://github.com/Guitarman9119/Raspberry-Pi-Pico-/tree/main/SSD1306%20OLED%20Display

i2c = I2C(0, scl = Pin(17), sda = Pin(16), freq=400000)
img = 'face mouth closed.pbm'
img2 = 'face eyes closed mouth closed.pbm'
img3 = ['face annoyed.pbm', 'face happy eyes mouth open.pbm', 'face eyes closed mouth open.pbm', 'face mouth open.pbm', 'face glitch1.pbm', 'face sleeping.pbm', 'face glitch2.pbm', 'face squint mouth closed.pbm', 'face glitch3.pbm', 'face squint mouth open.pbm', 'face glitch4.pbm', 'face worried.pbm', 'face happy eyes mouth closed.pbm', 'smile.pbm']
#img3 = 'face annoyed.pbm'


display = SSD1306_I2C(128, 64, i2c)
i = 0

while True:
    #open image, put your image here
    with open(img, 'rb') as f:
        f.readline() # number
        f.readline() # Creator
        f.readline() # Dimensions
        data = bytearray(f.read())
    
    fbuf = framebuf.FrameBuffer(data, 128, 64, framebuf.MONO_HLSB)

    display.invert(0)
    display.blit(fbuf, 0, 0)
    display.show()
    time.sleep(5)
    emote = random.choice(img3)
    i += 1
    glitch = random.randint(1,10)
    #print(random.randint(1,10))
    #    print(i)

    
    
    if glitch == 2:
        
        with open(emote, 'rb') as f:
           f.readline() # number
           f.readline() # Creator
           f.readline() # Dimensions
           data = bytearray(f.read())
    
        fbuf = framebuf.FrameBuffer(data, 128, 64, framebuf.MONO_HLSB)

        display.invert(0)
        display.blit(fbuf, 0, 0)
        display.show()
        time.sleep(2)
        i = i - i
        
    if i > 0:
        
        with open(img2, 'rb') as f:
           f.readline() # number
           f.readline() # Creator
           f.readline() # Dimensions
           data = bytearray(f.read())
    
        fbuf = framebuf.FrameBuffer(data, 128, 64, framebuf.MONO_HLSB)

        display.invert(0)
        display.blit(fbuf, 0, 0)
        display.show()
        time.sleep(.2)

        
    
    
    #random emotes after i = set number of loops a random emote is displayed for x sec i is reset to 0
    # use random.choice(img3) **add all emotes to img3** use random.randint(1,10)
    #set glitch animation to 10
