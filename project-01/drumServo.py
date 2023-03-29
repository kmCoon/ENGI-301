
"""
--------------------------------------------------------------------------
Servo Class
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

Init, Setup = Initializes servo class
driveMeasure = Drives servo through a designated pre-set measure

Somewhat based on code provided by Erik Welsh

"""

import time
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM

SG90_FREQ               = 50                  # 20ms period (50Hz)
SG90_POL                = 0                   # Rising Edge polarity
SG90_MIN_DUTY           = 5                   # 1ms pulse (5% duty cycle)  -- Fully clockwise (right)
SG90_MAX_DUTY           = 10                  # 2ms pulse (10% duty cycle) -- Fully anti-clockwise (left)

class Servo:
    isDriving = False
    measure = None
    
    def __init__(self, pin, drumtype, default_position=0):
        
        if (pin == None):
            raise ValueError("Pin not provided for Servo()")
        else:
            self.pin = pin
        if (drumtype == None):
            raise ValueError("Drumtype not provided for Servo()")
        else:
            self.drumtype = drumtype
            

        # Initialize the hardware components        
        self.position = default_position
        self._setup(default_position)
        
    
    # End def
    
    
    def _setup(self,default_position):
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
            
        #GPIO.setup(self.pin,GPIO.OUT)
        PWM.start(self.pin, self._duty_cycle_from_position(default_position), SG90_FREQ, SG90_POL)
        
        self.turn(default_position)
        
    #def get_position(self):
         #""" Return the position of the servo """
        #return self.position
        
        
    def turn(self, position):
        """ Turn Servo to the desired position based on percentage of motion range
    
          0% = Fully clockwise (right)
        100% = Fully anti-clockwise (left)      
        """
        # Record the current position
        self.position = position
        
        # Set PWM duty cycle based on position
        duty_cycle = ((SG90_MAX_DUTY - SG90_MIN_DUTY) * (position / 100)) + SG90_MIN_DUTY
        PWM.set_duty_cycle(self.pin, duty_cycle)