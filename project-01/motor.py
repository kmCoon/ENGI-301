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

import time

#import Adafruit_BBIO.GPIO as GPIO


class motor:
    isDriving = False
    measure = None
    
    def __init__(self, pin, drumtype):
        
        if (pin == None):
            raise ValueError("Pin not provided for Button()")
        else:
            self.pin = pin
        if (drumtype == None):
            raise ValueError("Drumtype not provided for Button()")
        else:
            self.drumtype = drumtype
            

        # Initialize the hardware components        
        self._setup()
    
    # End def
    
    
    def _setup(self):
        #GPIO.setup(self.pin,GPIO.IN)"""
        
        if self.drumtype == "hh":
            self.measure = [2,1,1]
            print("Successfully assigned")
        elif self.drumtype == "td":
            self.measure == [1,2,4,5]
            print("Successfully assigned")
        elif self.drumtype == "sd":
            self.measure == [1,2,2,5]
            print("Successfully assigned")
        else:
            raise ValueError("Drumtype not available!")
            
            
    def driveMeasure(self, beat=None):
        tempo = beat
        alpha = tempo/60
        print("Scalar = " + alpha)
        self.measure = [float(i) for i in self.measure]
        driveList = [alpha*value for value in self.measure]
        
        print(driveList)
        for i in driveList:
            print("I spin!")
            time.sleep(i)
                
    
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











