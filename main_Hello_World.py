# -*- coding: utf-8 -*-
__author__ = 'LiYuanhe'

from machine import Pin, SoftI2C
from lib_lcd1602_2004_with_i2c import LCD
scl_pin = 26
sda_pin = 27
lcd = LCD(SoftI2C(scl=Pin(scl_pin), sda=Pin(sda_pin), freq=100000))
lcd.puts("Hello, World!")