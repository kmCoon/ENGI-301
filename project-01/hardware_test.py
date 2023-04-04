#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
--------------------------------------------------------------------------
Hardware Test
--------------------------------------------------------------------------
License:   
Copyright 2023 - Kendall Cooney

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

"""

import ledGroup
import microphone
import motor
import button
import time
import threading
import drumServo

#p1_2

led1_pin = "P2_2"
led2_pin = "P2_4"
led3_pin = "P2_6"
led4_pin = "P2_8"
button_pin = "P2_34"
servohh_pin = "P1_36"
servotd_pin = "P1_33"
#mic_pin = ""

leds = ledGroup.LEDgroup(led1_pin,led2_pin,led3_pin,led4_pin)
mic = microphone.Microphone()
tuneButton = button.Button(button_pin)
s1 = drumServo.Servo(servohh_pin,"hh")
s2 = drumServo.Servo(servotd_pin,"td")


#s1.cleanup()

try: 
    while (True):
    #with sd.InputStream(channels = 1, callback=print_sound):
    
        if (tuneButton.is_pressed() == True):
            t1 = threading.Thread(target = leds.blink_4_time, args=[0.5,5])
            t2 = threading.Thread(target = s1.runMeasure,args = [])
            t3 = threading.Thread(target = s2.runMeasure,args= [])
            t1.start()
            t2.start()
            t3.start()
            
            t1.join()
            t2.join()
            t3.join()

except KeyboardInterrupt:
    print("Exception caught")
    s1.cleanup()
    s2.cleanup()
    exit()
    #mic.audioRead(44100,5)
    #print(str(mic.audioRead(44100,5)))
    

"""
 

micPin = "P1_1"

m1 = microphone.Microphone("")


leds = ledGroup.LEDgroup(led1_pin,led2_pin,led3_pin,led4_pin)
hh_motor = Motor.motor(5,"hh")
td_motor = Motor.motor(6,"td")

leds.all_On()
time.sleep(2)
leds.all_Off()
time.sleep(1)

leds.blink_sequentially(1)
time.sleep(1)

leds.blink_together(1)
leds.blink_together(1)

t1 = threading.Thread(target= hh_motor.drive4, args=(2,))
t2 = threading.Thread(target= td_motor.drive4, args=(2,))

t1.start()
t2.start()

t1.join()
t2.join()
"""

    
    