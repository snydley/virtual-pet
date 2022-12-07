from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf
import time
import random

# display code sourced from https://github.com/Guitarman9119/Raspberry-Pi-Pico-/tree/main/SSD1306%20OLED%20Display

i2c = I2C(0, scl = Pin(17), sda = Pin(16), freq=400000)
img = 'face mouth closed.pbm'
img2 = 'face eyes closed mouth closed.pbm'
img3 = ['face annoyed.pbm', 'face happy eyes mouth open.pbm', 'face eyes closed mouth open.pbm', 'face mouth open.pbm', 'face squint mouth closed.pbm', 'face squint mouth open.pbm', 'face worried.pbm', 'face happy eyes mouth closed.pbm', 'smile.pbm']
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
    time.sleep(3) # cycle speed
    emogfx = random.choice(img3)
    i += 1 # cycle counter
    emote = random.randint(1,5) # chance of emote
    #print(random.randint(1,10))
    print(i)
        
    if i >=20:
        # no emotes in 20 cycles degyo falls asleep
        with open('face sleeping.pbm', 'rb') as f:
           f.readline() # number
           f.readline() # Creator
           f.readline() # Dimensions
           data = bytearray(f.read())
    
        fbuf = framebuf.FrameBuffer(data, 128, 64, framebuf.MONO_HLSB)

        display.invert(0)
        display.blit(fbuf, 0, 0)
        display.show()
        time.sleep(60)
        i = i - i

    if i == 10:
        with open('face glitch1.pbm', 'rb') as f:
           f.readline() # number
           f.readline() # Creator
           f.readline() # Dimensions
           data = bytearray(f.read())
    
        fbuf = framebuf.FrameBuffer(data, 128, 64, framebuf.MONO_HLSB)

        display.invert(0)
        display.blit(fbuf, 0, 0)
        display.show()
        time.sleep(0.05)
        
        with open('face glitch2.pbm', 'rb') as f:
           f.readline() # number
           f.readline() # Creator
           f.readline() # Dimensions
           data = bytearray(f.read())
    
        fbuf = framebuf.FrameBuffer(data, 128, 64, framebuf.MONO_HLSB)

        display.invert(0)
        display.blit(fbuf, 0, 0)
        display.show()
        time.sleep(0.05)
        
        with open('face glitch3.pbm', 'rb') as f:
           f.readline() # number
           f.readline() # Creator
           f.readline() # Dimensions
           data = bytearray(f.read())
    
        fbuf = framebuf.FrameBuffer(data, 128, 64, framebuf.MONO_HLSB)

        display.invert(0)
        display.blit(fbuf, 0, 0)
        display.show()
        time.sleep(0.5)
        
        with open('face glitch4.pbm', 'rb') as f:
           f.readline() # number
           f.readline() # Creator
           f.readline() # Dimensions
           data = bytearray(f.read())
    
        fbuf = framebuf.FrameBuffer(data, 128, 64, framebuf.MONO_HLSB)

        display.invert(0)
        display.blit(fbuf, 0, 0)
        display.show()
        time.sleep(0.05)
    
    if emote == 1:
        
        with open(emogfx, 'rb') as f:
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

        
    
    
    #set glitch animation to 10


