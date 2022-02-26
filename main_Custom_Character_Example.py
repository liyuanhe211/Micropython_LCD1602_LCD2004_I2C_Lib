# -*- coding: utf-8 -*-
__author__ = 'LiYuanhe'

from machine import Pin, Signal, SoftI2C
import time
import socket
import machine
import network
import micropython
import os
from lib_lcd1602_2004_with_i2c import LCD

micropython.alloc_emergency_exception_buf(100)

scl_pin = 26
sda_pin = 27
lcd = LCD(SoftI2C(scl=Pin(scl_pin), sda=Pin(sda_pin), freq=100000))

custom_char_0 = [
  0b00000,
  0b00000,
  0b00000,
  0b00000,
  0b00000,
  0b00000,
  0b00001,
  0b00011]

custom_char_1 = [
  0b00111,
  0b00111,
  0b01110,
  0b01110,
  0b01110,
  0b11110,
  0b11111,
  0b11111]

custom_char_2 = [
  0b00000,
  0b00001,
  0b00111,
  0b01111,
  0b11111,
  0b11110,
  0b11000,
  0b10000]

custom_char_3 = [
  0b00000,
  0b00000,
  0b00000,
  0b00000,
  0b00000,
  0b00000,
  0b11111,
  0b11111]

custom_char_4 = [
  0b01111,
  0b11111,
  0b11111,
  0b11000,
  0b00000,
  0b00000,
  0b00000,
  0b00000]

custom_char_5 = [
  0b11100,
  0b11110,
  0b11111,
  0b00011,
  0b00001,
  0b00000,
  0b00000,
  0b00000]

custom_char_6 = [
  0b00000,
  0b00000,
  0b10000,
  0b11100,
  0b11110,
  0b01111,
  0b00111,
  0b00011]

custom_char_7 = [
  0b11000,
  0b11000,
  0b11100,
  0b11100,
  0b11100,
  0b11110,
  0b11110,
  0b11110]


lcd.create_charactor(0,custom_char_0)
lcd.create_charactor(1,custom_char_1)
lcd.create_charactor(2,custom_char_2)
lcd.create_charactor(3,custom_char_3)
lcd.create_charactor(4,custom_char_4)
lcd.create_charactor(5,custom_char_5)
lcd.create_charactor(6,custom_char_6)
lcd.create_charactor(7,custom_char_7)

top = chr(0)+chr(2)+chr(4)+chr(5)+chr(6)+' '
down = chr(1)+chr(3)+chr(3)+chr(3)+chr(3)+chr(7)
count=0
while True:
    line1 = " "*count + top + (16-count-6)*' '
    line2 = " "*count + down + (16-count-6)*' '
    count+=1
    lcd.puts(line1,0)
    lcd.puts(line2,1)
    time.sleep(0.3)
    if count==11:
        break

line1 = " LCD1602  " + top
line2 = "Custom chr" + down
lcd.puts(line1,0)
lcd.puts(line2,1)