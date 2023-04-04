
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

SG90_FREQ               = 333                  # 3 ms period (33Hz)
SG90_POL                = 0                   # Rising Edge polarity
SG90_MIN_DUTY           = 24                  # 700us pulse (24% duty cycle)  -- Fully clockwise (right)
SG90_MAX_DUTY           = 76                  # 2300us pulse (75% duty cycle) -- Fully counter-clockwise (left)
servo_pin = "P1_36"

class Servo:
    isDriving = False
    measure = None
    speed = None
    
    def __init__(self, pin, drumtype, default_speed=0):
        
        if (pin == None):
            raise ValueError("Pin not provided for Servo()")
        else:
            self.pin = pin
        if (drumtype == None):
            raise ValueError("Drumtype not provided for Servo()")
        else:
            self.drumtype = drumtype
            

        # Initialize the hardware components        
        self.speed = default_speed
        self._setup(default_speed)
        
    
    # End def
    
    
    def _setup(self,default_speed):
        #GPIO.setup(self.pin,GPIO.IN)"""
        
        if self.drumtype == "hh":
            self.measure = [1,1,1,1]
            print("Successfully assigned")
        elif self.drumtype == "td":
            self.measure == [0.1,1,1]
            print("Successfully assigned")
        elif self.drumtype == "sd":
            self.measure == [1,2,2,5]
            print("Successfully assigned")
        else:
            raise ValueError("Drumtype not available!")
            
        #GPIO.setup(self.pin,GPIO.OUT)
        PWM.start(self.pin, SG90_MIN_DUTY, SG90_FREQ, SG90_POL)
        self.setSpeed(default_speed)
        
    #def get_position(self):
         #""" Return the position of the servo """
        #return self.position
        
        
    def setSpeed(self, speed):
        """ Set speed of Servo to the desired position based on percentage of motion range
    
          0% = Fully clockwise (right)
        100% = Fully anti-clockwise (left)      
        """
        # Record the current position
        self.speed = speed
        
        # Set PWM duty cycle based on position
        #duty_cycle = ((SG90_MAX_DUTY - SG90_MIN_DUTY) * (position / 100)) + SG90_MIN_DUTY
        duty_cycle = (speed/100)*(47) + 48  # -100 > 24, +100 = 76
        print(duty_cycle)
        PWM.set_duty_cycle(self.pin, duty_cycle)
        
    def strike(self):
        vroom = 100
        self.setSpeed(vroom)
        time.sleep(0.10)
        self.setSpeed(-vroom)
        time.sleep(0.10)
        self.setSpeed(0)
        
    def runMeasure(self,bpm):
        # Each measure rated for 60 bpm... If you want to go 120 bpm, must DECREASE wait time
        # by factor of 2. Thus, alpha = 1/(bpm/60)
        
        alpha = 1/(bpm/60)
        
        notes = self.measure
        for i in notes:
            self.strike()
            wait = i*alpha
            time.sleep(wait)
        
    def cleanup(self):
        """Cleanup the hardware components."""
        # Stop servo
        PWM.stop(self.pin)
        PWM.cleanup()
        

if __name__ == "__main__":
    s1 = Servo(servo_pin,"hh",0)
    
    for i in range(100):
        print("{0}".format(i))
        PWM.set_duty_cycle(servo_pin, i)
        time.sleep(1)
    s1.cleanup()

