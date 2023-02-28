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

"""

import time

#import Adafruit_BBIO.GPIO as GPIO

class LEDgroup():
    """ Motor Class """
    
    def __init__(self, pinn1,pinn2,pinn3,pinn4):
        
        if (pinn1 == None):
            raise ValueError("Pin not provided for LED 1!")
        elif (pinn2 == None):
            raise ValueError("Pin not provided for LED 2!")
        elif (pinn3 == None):
            raise ValueError("Pin not provided for LED 3!")
        elif (pinn4 == None):
            raise ValueError("Pin not provided for LED 4!")
        else:
            self.pin1 = str(pinn1)
            self.pin2 = str(pinn2)
            self.pin3 = str(pinn3)
            self.pin4 = str(pinn4)
        
        # Initialize the hardware components        
        self._setup()
    
    # End def
    
    
    def _setup(self):
        """ Setup the hardware components. """
        # Initialize Button
        # Set 60 bpm rhythm 
        print("Pins have been set up!")
        """GPIO.setup(self.pin1,GPIO.IN)
        GPIO.setup(self.pin2,GPIO.IN)
        GPIO.setup(self.pin3,GPIO.IN)
        GPIO.setup(self.pin4,GPIO.IN)"""


    def blink_together(self, delta):
        
        print("PIN " + self.pin1 + ", PIN " + self.pin2 + ", PIN " + self.pin3 + ", PIN " + self.pin4 + " ON")
        """GPIO.output(self.pin1, GPIO.HIGH)
        GPIO.output(self.pin2, GPIO.HIGH)
        GPIO.output(self.pin3, GPIO.HIGH)
        GPIO.output(self.pin4, GPIO.HIGH)"""
        
        time.sleep(delta)
        
        print("PIN " + self.pin1 + ",PIN " + self.pin2 + ",PIN " + self.pin3 + ",PIN " + self.pin4 + " OFF")
        """GPIO.output(self.pin1, GPIO.LOW)
        GPIO.output(self.pin2, GPIO.LOW)
        GPIO.output(self.pin3, GPIO.LOW)
        GPIO.output(self.pin4, GPIO.LOW)"""
        
        time.sleep(delta)
        
    def blink_sequentially(self, delta):
        print("PIN1 ON")
        #GPIO.output(self.pin1, GPIO.HIGH)
        time.sleep(delta)
        print("PIN2 ON")
        #GPIO.output(self.pin2, GPIO.HIGH)
        time.sleep(delta)
        print("PIN3 ON")
        #GPIO.output(self.pin3, GPIO.HIGH)
        time.sleep(delta)
        print("PIN4 ON")
        #GPIO.output(self.pin4, GPIO.HIGH)
        time.sleep(delta)
        print("All off")
        """GPIO.output(self.pin1, GPIO.LOW)
        GPIO.output(self.pin2, GPIO.LOW)
        GPIO.output(self.pin3, GPIO.LOW)
        GPIO.output(self.pin4, GPIO.LOW)"""
        
    def all_On(self):
        print("All on")
        """GPIO.output(self.pin1, GPIO.HIGH)
        GPIO.output(self.pin2, GPIO.HIGH)
        GPIO.output(self.pin3, GPIO.HIGH)
        GPIO.output(self.pin4, GPIO.HIGH)"""
        
    def all_Off(self):
        print("All off")
        """GPIO.output(self.pin1, GPIO.LOW)
        GPIO.output(self.pin2, GPIO.LOW)
        GPIO.output(self.pin3, GPIO.LOW)
        GPIO.output(self.pin4, GPIO.LOW)"""
    





