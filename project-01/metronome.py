#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
--------------------------------------------------------------------------
Metronome Class
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

1) Start with idle... Default metronome is OFF
    Turn on LEDs 
    Wait for button signal
    
2) If button pressed...
    Begin signal processing
    Blink all LEDs
    
3) When metronome ON...
    Play music! 
    
"""

import drumServo
import ledGroup
import button
import threading

print("Program start!")


led1_pin = "P2_2"
led2_pin = "P2_4"
led3_pin = "P2_6"
led4_pin = "P2_8"
button_pin = "P2_34"
servohh_pin = "P1_36"
servotd_pin = "P1_33"


leds = ledGroup.LEDgroup(led1_pin,led2_pin,led3_pin,led4_pin)
hh_s = drumServo.Servo(servohh_pin,"hh")
td_s = drumServo.Servo(servotd_pin,"td")
t_button = button.Button(button_pin)

tuning = False
playing = True
scalar = 1
bpm = 60

input_thread = True
check_For_Butt = True

leds.all_Off()

def blink_Until():
    global tuning
    global input_thread
    while input_thread == True:
        leds.blink_sequentially(0.25)
        
def checkButt():
    global check_For_Butt
    global tuning
    global playing
    while True:
        if (t_button.is_pressed() == True):
            #print("button press detected!")
            playing = False
            tuning = True
            check_For_Butt = False
            break
            
def blink_LongTime():
    global check_For_Butt
    while check_For_Butt == True:
        leds.blink_together(0.25)
    
    
def take_Input():
    global bpm
    global input_thread
    user_input = input("Please type desired BPM: ")
    bpm = int(user_input)
    input_thread = False
    print("Input taken")
        

try:
        
    while(True):
    #    global tuning

        if tuning == True:
            print("I started tuning!")
            input_thread = True
            #leds.blink_sequentially(0.5)
            playing = False
            
            t_t1 = threading.Thread(target = blink_Until, args=[])
            t_t2 = threading.Thread(target = take_Input, args=[])
            
            #scalar = sampleAudio.analyze(); """
            t_t2.start()
            t_t1.start()
            
            t_t2.join()
            input_thread = False
            
            tuning = False
            playing = True
            
            t_t1.join()
    
        while playing == True:
            check_For_Butt = True
            beta = (int(bpm))/60
            
            p_t1 = threading.Thread(target=checkButt, args=[])
            p_t2 = threading.Thread(target=leds.blink_together,args=[beta])
            
            p_t1.start()
            p_t2.start()
            
            if check_For_Butt == False:
                p_t1.join()
                p_t2.join()
                print("I broke the butt loop")
                break
            
            #t1 = threading.Thread(target = leds.blink_4_time, args=[0.5,5])
            #t2 = threading.Thread(target = s1.runMeasure,args = [])
            #t3 = threading.Thread(target = s2.runMeasure,args= [])
            """"drive all motors"""

except KeyboardInterrupt:
    print("Exception caught")
    hh_s.cleanup()
    td_s.cleanup
    leds.all_Off()
    exit()
    #mic.audioRead(44100,5)
    #print(str(mic.audioRead(44100,5)))
        
        
        

    














