#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  keypad.py
#  
#  Copyright 2020  <pi@raspberrypi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import RPi.GPIO as GPIO
import time
from neopixel import *
import argparse

# LED strip configuration:
LED_COUNT      = 16      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 200     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

buzz=16

line1 = 6
line2 = 5
line3 = 4
line4 = 17
line5 = 27
line6 = 22
line7 = 10
line8 = 9

global button
press = ""

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(line1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(line2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(line3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(line4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(line5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(line6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(line7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(line8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(buzz, GPIO.OUT)

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)

# def getButton():
    # button = ""
    # if ((GPIO.input(line1) == GPIO.LOW) and (GPIO.input(line5) == GPIO.LOW)):
        # print("*")
        # while ((GPIO.input(line1) == GPIO.LOW) and (GPIO.input(line5) == GPIO.LOW)):
            # time.sleep(0.1)
        # #print("*")
        # button = "*"
    # if ((GPIO.input(line1) == GPIO.LOW) and (GPIO.input(line6) == GPIO.LOW)):
        # print("0")
        # while (((GPIO.input(line1) == GPIO.LOW) and (GPIO.input(line6) == GPIO.LOW)):
            # time.sleep(0.1)
        # button = "0"
    # if ((GPIO.input(line1) == GPIO.LOW) and (GPIO.input(line7) == GPIO.LOW)):
        # print("#")
        # while ((GPIO.input(line1) == GPIO.LOW) and (GPIO.input(line7) == GPIO.LOW)):
            # time.sleep(0.1)
        # button = "#"
    # if ((GPIO.input(line1) == GPIO.LOW) and (GPIO.input(line8) == GPIO.LOW)):
        # print("D")
        # while ((GPIO.input(line1) == GPIO.LOW) and (GPIO.input(line8) == GPIO.LOW)):
            # time.sleep(0.1)
        # button = "D"
        
        
    # if ((GPIO.input(line2) == GPIO.LOW) and (GPIO.input(line5) == GPIO.LOW)):
        # print("7")
        # while ((GPIO.input(line2) == GPIO.LOW) and (GPIO.input(line5) == GPIO.LOW)):
            # time.sleep(0.1)
        # button = "7"
    # if ((GPIO.input(line2) == GPIO.LOW) and (GPIO.input(line6) == GPIO.LOW)):
        # print("8")
        # while ((GPIO.input(line2) == GPIO.LOW) and (GPIO.input(line6) == GPIO.LOW)):
            # time.sleep(0.1)
        # button = "8"
    # if ((GPIO.input(line2) == GPIO.LOW) and (GPIO.input(line7) == GPIO.LOW)):
        # print("9")
        # while ((GPIO.input(line2) == GPIO.LOW) and (GPIO.input(line7) == GPIO.LOW)):
            # time.sleep(0.1)
        # button = "9"
    # if ((GPIO.input(line2) == GPIO.LOW) and (GPIO.input(line8) == GPIO.LOW)):
        # print("C")
        # while ((GPIO.input(line2) == GPIO.LOW) and (GPIO.input(line8) == GPIO.LOW)):
            # time.sleep(0.1)
        # button = "C"
        
    # if ((GPIO.input(line3) == GPIO.LOW) and (GPIO.input(line5) == GPIO.LOW)):
        # print("4")
        # while ((GPIO.input(line3) == GPIO.LOW) and (GPIO.input(line5) == GPIO.LOW)):
            # time.sleep(0.1)
        # button = "4"
    # if ((GPIO.input(line3) == GPIO.LOW) and (GPIO.input(line6) == GPIO.LOW)):
        # print("5")
        # while ((GPIO.input(line3) == GPIO.LOW) and (GPIO.input(line6) == GPIO.LOW)):
            # time.sleep(0.1)
        # button = "5"
    # if ((GPIO.input(line3) == GPIO.LOW) and (GPIO.input(line7) == GPIO.LOW)):
        # print("6")
        # while ((GPIO.input(line3) == GPIO.LOW) and (GPIO.input(line7) == GPIO.LOW)):
            # time.sleep(0.1)
        # button = "6"
    # if ((GPIO.input(line3) == GPIO.LOW) and (GPIO.input(line8) == GPIO.LOW)):
        # print("B")
        # while ((GPIO.input(line3) == GPIO.LOW) and (GPIO.input(line8) == GPIO.LOW)):
            # time.sleep(0.1)
        # button = "B"
        
    # if ((GPIO.input(line4) == GPIO.LOW) and (GPIO.input(line5) == GPIO.LOW)):
        # print("1")
        # while ((GPIO.input(line4) == GPIO.LOW) and (GPIO.input(line5) == GPIO.LOW)):
            # time.sleep(0.1)
        # button = "1"
    # if ((GPIO.input(line4) == GPIO.LOW) and (GPIO.input(line6) == GPIO.LOW)):
        # print("2")
        # while ((GPIO.input(line4) == GPIO.LOW) and (GPIO.input(line6) == GPIO.LOW)):
            # time.sleep(0.1)
        # button = "2"
    # if ((GPIO.input(line4) == GPIO.LOW) and (GPIO.input(line7) == GPIO.LOW)):
        # print("3")
        # while ((GPIO.input(line4) == GPIO.LOW) and (GPIO.input(line7) == GPIO.LOW)):
            # time.sleep(0.1)
        # button = "3"
    # if ((GPIO.input(line4) == GPIO.LOW) and (GPIO.input(line8) == GPIO.LOW)):
        # print("A")
        # while ((GPIO.input(line4) == GPIO.LOW) and (GPIO.input(line8) == GPIO.LOW)):
            # time.sleep(0.1)
        # button = "A"
        
    # return button

def beep():
    GPIO.output(buzz, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(buzz, GPIO.LOW)

def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()
    GPIO.output(buzz, GPIO.LOW)

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()
    
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0, 0, 255))
        strip.show()
        time.sleep(0.1)
        print(i)

    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()
                
    print("System Ready")
    while True:
        
        
        # if(GPIO.input(line1) == GPIO.LOW):
            # print("line1")
        # if(GPIO.input(line2) == GPIO.LOW):
            # print("line2")
        # if(GPIO.input(line3) == GPIO.LOW):
            # print("line3")
        # if(GPIO.input(line4) == GPIO.LOW):
            # print("line4")
        # if(GPIO.input(line5) == GPIO.LOW):
            # print("line5")
        # if(GPIO.input(line6) == GPIO.LOW):
            # print("line6")
        # if(GPIO.input(line7) == GPIO.LOW):
            # print("line7")
        # if(GPIO.input(line8) == GPIO.LOW):
            # print("line8")

    
        if ((GPIO.input(line1) == GPIO.LOW) and (GPIO.input(line5) == GPIO.LOW)):
            print("*")
            button = "*"
            
            while ((GPIO.input(line1) == GPIO.LOW) and (GPIO.input(line5) == GPIO.LOW)):
                time.sleep(0.1)
                strip.setPixelColor(0, Color(255, 255, 255))
                strip.show()
            strip.setPixelColor(0, Color(0, 0, 0))
            strip.show()
            beep()
        
        if ((GPIO.input(line2) == GPIO.LOW) and (GPIO.input(line5) == GPIO.LOW)):
            print("0")
            button = "0"
            
            while ((GPIO.input(line2) == GPIO.LOW) and (GPIO.input(line5) == GPIO.LOW)):
                time.sleep(0.1)
                strip.setPixelColor(1, Color(255, 255, 255))
                strip.show()
            strip.setPixelColor(1, Color(0, 0, 0))
            strip.show()
            beep()
        
        if ((GPIO.input(line3) == GPIO.LOW) and (GPIO.input(line5) == GPIO.LOW)):
            print("#")
            button = "#"
            
            while ((GPIO.input(line3) == GPIO.LOW) and (GPIO.input(line5) == GPIO.LOW)):
                time.sleep(0.1)
                strip.setPixelColor(2, Color(255, 255, 255))
                strip.show()
            strip.setPixelColor(2, Color(0, 0, 0))
            strip.show()
            beep()
            
        if ((GPIO.input(line4) == GPIO.LOW) and (GPIO.input(line5) == GPIO.LOW)):
            print("D")
            button = "D"
            
            while ((GPIO.input(line4) == GPIO.LOW) and (GPIO.input(line5) == GPIO.LOW)):
                time.sleep(0.1)
                strip.setPixelColor(3, Color(255, 255, 255))
                strip.show()
            strip.setPixelColor(3, Color(0, 0, 0))
            strip.show()
            beep()

            
        if ((GPIO.input(line1) == GPIO.LOW) and (GPIO.input(line6) == GPIO.LOW)):
            print("7")
            button = "7"
            
            while ((GPIO.input(line1) == GPIO.LOW) and (GPIO.input(line6) == GPIO.LOW)):
                time.sleep(0.1)
                strip.setPixelColor(7, Color(255, 255, 255))
                strip.show()
            strip.setPixelColor(7, Color(0, 0, 0))
            strip.show()
            beep()
            
        if ((GPIO.input(line2) == GPIO.LOW) and (GPIO.input(line6) == GPIO.LOW)):
            print("8")
            button = "8"
            
            while ((GPIO.input(line2) == GPIO.LOW) and (GPIO.input(line6) == GPIO.LOW)):
                time.sleep(0.1)
                strip.setPixelColor(6, Color(255, 255, 255))
                strip.show()
            strip.setPixelColor(6, Color(0, 0, 0))
            strip.show()
            beep()
            
        if ((GPIO.input(line3) == GPIO.LOW) and (GPIO.input(line6) == GPIO.LOW)):
            print("9")
            button = "9"
            
            while ((GPIO.input(line3) == GPIO.LOW) and (GPIO.input(line6) == GPIO.LOW)):
                time.sleep(0.1)
                strip.setPixelColor(5, Color(255, 255, 255))
                strip.show()
            strip.setPixelColor(5, Color(0, 0, 0))
            strip.show()
            beep()
            
        if ((GPIO.input(line4) == GPIO.LOW) and (GPIO.input(line6) == GPIO.LOW)):
            print("C")
            button = "C"
            
            while ((GPIO.input(line4) == GPIO.LOW) and (GPIO.input(line6) == GPIO.LOW)):
                time.sleep(0.1)
                strip.setPixelColor(4, Color(255, 255, 255))
                strip.show()
            strip.setPixelColor(4, Color(0, 0, 0))
            strip.show()
            beep()
            
        if ((GPIO.input(line1) == GPIO.LOW) and (GPIO.input(line7) == GPIO.LOW)):
            print("4")
            button = "4"
            
            while ((GPIO.input(line1) == GPIO.LOW) and (GPIO.input(line7) == GPIO.LOW)):
                time.sleep(0.1)
                strip.setPixelColor(8, Color(255, 255, 255))
                strip.show()
            strip.setPixelColor(8, Color(0, 0, 0))
            strip.show()
            beep()
            
        if ((GPIO.input(line2) == GPIO.LOW) and (GPIO.input(line7) == GPIO.LOW)):
            print("5")
            button = "5"
            
            while ((GPIO.input(line2) == GPIO.LOW) and (GPIO.input(line7) == GPIO.LOW)):
                time.sleep(0.1)
                strip.setPixelColor(9, Color(255, 255, 255))
                strip.show()
            strip.setPixelColor(9, Color(0, 0, 0))
            strip.show()
            beep()
            
        if ((GPIO.input(line3) == GPIO.LOW) and (GPIO.input(line7) == GPIO.LOW)):
            print("6")
            button = "6"
            
            while ((GPIO.input(line3) == GPIO.LOW) and (GPIO.input(line7) == GPIO.LOW)):
                time.sleep(0.1)
                strip.setPixelColor(10, Color(255, 255, 255))
                strip.show()
            strip.setPixelColor(10, Color(0, 0, 0))
            strip.show()
            beep()
            
        if ((GPIO.input(line4) == GPIO.LOW) and (GPIO.input(line7) == GPIO.LOW)):
            print("B")
            button = "B"
            
            while ((GPIO.input(line4) == GPIO.LOW) and (GPIO.input(line7) == GPIO.LOW)):
                time.sleep(0.1)
                strip.setPixelColor(11, Color(255, 255, 255))
                strip.show()
            strip.setPixelColor(11, Color(0, 0, 0))
            strip.show()
            beep()
                
        if ((GPIO.input(line1) == GPIO.LOW) and (GPIO.input(line8) == GPIO.LOW)):
            print("1")
            button = "1"
           
            while ((GPIO.input(line1) == GPIO.LOW) and (GPIO.input(line8) == GPIO.LOW)):
                strip.setPixelColor(15, Color(255, 255, 255))
                strip.show()
                time.sleep(0.1)
            strip.setPixelColor(15, Color(0, 0, 0))
            strip.show()
            beep()
            
        if ((GPIO.input(line2) == GPIO.LOW) and (GPIO.input(line8) == GPIO.LOW)):
            print("2")
            button = "2"
            
            while ((GPIO.input(line2) == GPIO.LOW) and (GPIO.input(line8) == GPIO.LOW)):
                strip.setPixelColor(14, Color(255, 255, 255))
                strip.show()
                time.sleep(0.1)
            strip.setPixelColor(14, Color(0, 0, 0))
            strip.show()
            beep()
            
        if ((GPIO.input(line3) == GPIO.LOW) and (GPIO.input(line8) == GPIO.LOW)):
            print("3")
            button = "3"
            
            while ((GPIO.input(line3) == GPIO.LOW) and (GPIO.input(line8) == GPIO.LOW)):
                strip.setPixelColor(13, Color(255, 255, 255))
                strip.show()
                time.sleep(0.1)
            strip.setPixelColor(13, Color(0, 0, 0))
            strip.show()
            beep()
            
        if ((GPIO.input(line4) == GPIO.LOW) and (GPIO.input(line8) == GPIO.LOW)):
            print("A")
            button = "A"
            
            while ((GPIO.input(line4) == GPIO.LOW) and (GPIO.input(line8) == GPIO.LOW)):
                time.sleep(0.1)
                strip.setPixelColor(12, Color(255, 255, 255))
                strip.show()
            strip.setPixelColor(12, Color(0, 0, 0))
            strip.show()
            beep()
        

        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
