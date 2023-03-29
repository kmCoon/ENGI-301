#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
--------------------------------------------------------------------------
Microphone Class
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

#from scipy import fft 
import numpy as np
import Adafruit_BBIO.GPIO as GPIO
#import matplotlib.pyplot as plt
#from scipy.signal import find_peaks
import sounddevice as sd

class Microphone():
    """ Motor Class """
    
    def __init__(self):
        
        #if (pin == None):
         #   raise ValueError("Pin not provided for microphone!")
        
        
        # Initialize the hardware components        
        self._setup()


    def _setup(self):
        """ Setup the hardware components. """
        #GPIO.setup(self.pin,GPIO.IN)
        
        sd.default.device = 0
        sd.default.channels = 1
        
        print("Wow I set up pins.")
        
        
        
    def audioRead(self,fs,duration):
        #Read audio here!
        
        myrecording = sd.rec(duration * fs, samplerate=fs,blocking=True)
        np.save("trial1.txt",myrecording)
        print(np.size(myrecording))
        return myrecording
        
        """
        
    def extractTempo(self):
        Fs = 800 # Sample rsuate in Hz
        t = 0.75 # Duration in seconds
        audio = self.audioRead(Fs,t)
        y = sc.fft(audio)
        y = abs(y)
        N = len(y)
        T = 1/Fs
        xf = fft.fftfreq(N,T)
        plt.plot(xf,y)
        
        peakX,Properties = find_peaks(y,prominence=1)
        print(str(xf[peakX]))
        
        plt.plot(xf[peakX], y[peakX])
        
        """
        
        
        

    
    
    
    
    
    
    
    
    