#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 20:45:18 2023

@author: kendallcooney
"""

import motor as Motor
import time as time

motor_pin = "P2_10"

m1 = Motor.motor(motor_pin,"hh")
m1.drive4(3)
