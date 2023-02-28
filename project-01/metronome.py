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

import motor as Motor
import LEDgroup as LEDGroup
import button as Button

print("Program start!")

led = LEDGroup(1,2,3,4)
hh_motor = Motor(7,"hh")
td_motor = Motor(9,"td")
sd_motor = Motor(10,"sd")
button = Button(11)

tuning = False
playing = False
scalar = 1

led.all_On()

while(True):
    if tuning == True:
        led.blink_sequentially()
        playing = False
        """" scalar = sampleAudio.analyze(); """
        playing = True

    while playing == True:
        if (Button.is_Pressed == True):
            playing = False
            tuning = True
            break
        """"drive all motors"""
        
        
        
        
        

    














