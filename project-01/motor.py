#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
--------------------------------------------------------------------------
Motor Class
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

Init, Setup = Initializes motor class
driveMeasure = Drives motor through a designated pre-set measure

"""


"""
    SIMPLE DRUM MEASURES [Array represents time to wait BEFORE AND AFTER beat]
    
Tom Drum -- (Quarter, rest, quarter, rest): (0,1, 0,1)
High hat -- (Eigth notes): (0,0.5, 0,0.5, 0,0.5, 0,0.5, 0,0.5, 0,0.5, 0,0.5, 0,0.5,)
Snare drum -- (1,0, 1,0)






"""

import time
#import Adafruit_BBIO.GPIO as GPIO


class motor:
    isDriving = False
    measure = None
    driveList = None
    
    def __init__(self, pin, drumtype):
        
        if (pin == None):
            raise ValueError("Pin not provided")
        else:
            self.pin = pin
        if (drumtype == None):
            raise ValueError("Drumtype not provided")
        else:
            self.drumtype = drumtype
            

        # Initialize the hardware components        
        self._setup()
    
    # End def
    
    
    def _setup(self):
        #GPIO.setup(self.pin,GPIO.OUT)
        
        if self.drumtype == "hh":
            self.measure = [0,0.5, 0,0.5, 0,0.5, 0,0.5, 0,0.5, 0,0.5, 0,0.5, 0,0.5]
            print("Successfully assigned")
            
        elif self.drumtype == "td":
            self.measure = [0,1, 0,1]
            print("Successfully assigned")
            
        elif self.drumtype == "sd":
            self.measure = [1,0, 1,0]
            print("Successfully assigned")
            
        else:
            raise ValueError("Drumtype not available!")
        print(str(self.measure))
            
            
    def driveMeasure(self, beat):
        alpha = beat/60
        print("Scalar = " + str(alpha))
        alphaMeasure = [float(k) for k in self.measure]
        self.driveList = [alpha*value for value in alphaMeasure]
        
        i_end = len(self.measure) - 1
        print(self.driveList)
        for j in range(10):
            for i in range(i_end):
                time.sleep(self.driveList[i])
                print("I spin!")
                time.sleep(self.driveList[i+1])
                
    
    def drive4(self, duration=None):
        #GPIO.output(self.pin, GPIO.HIGH)
        print("GPIO High")
        time.sleep(duration)
        print("GPIO Low")
        #GPIO.output(self.pin, GPIO.LOW)
        
    def pulse(self,duration,Hz):
        onCycle = (1/2)*(1/Hz)
        offCycle = onCycle
        tim = time.time()
        while time.time() < (tim + duration):
            print("GPIO High")
            #GPIO.output(self.pin, GPIO.HIGH)
            time.sleep(onCycle)
            #GPIO.output(self.pin, GPIO.LOW)
            print("GPIO Low")
            time.sleep(offCycle)
      

# End class











