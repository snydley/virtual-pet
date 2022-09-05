from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf
import time


i2c = I2C(0, scl = Pin(17), sda = Pin(16), freq=400000)
img = 'face mouth closed.pbm'
img2 = 'face eyes closed mouth closed.pbm'
img3 = 'face happy eyes mouth closed.pbm'
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
    i += 1
    print(i)
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
    
    #random emotes after i = set number of loops a random emote is displayed for 1 sec i is reset to 0
    
    if i == 5:
        
        with open(img3, 'rb') as f:
           f.readline() # number
           f.readline() # Creator
           f.readline() # Dimensions
           data = bytearray(f.read())
    
        fbuf = framebuf.FrameBuffer(data, 128, 64, framebuf.MONO_HLSB)

        display.invert(0)
        display.blit(fbuf, 0, 0)
        display.show()
        time.sleep(1) 
