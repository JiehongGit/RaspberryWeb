#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import requests
import json

def DHT11():
  channel = 24
  data = []
  j = 0

  GPIO.setmode(GPIO.BCM)
  time.sleep(1)
  GPIO.setup(channel, GPIO.OUT)
  GPIO.output(channel, GPIO.LOW)
  time.sleep(0.02)
  GPIO.output(channel, GPIO.HIGH)
  GPIO.setup(channel, GPIO.IN)

  while GPIO.input(channel) == GPIO.LOW:
       continue

  while GPIO.input(channel) == GPIO.HIGH:
       continue

  while j < 40:
       k = 0
       while GPIO.input(channel) == GPIO.LOW:
           continue

       while GPIO.input(channel) == GPIO.HIGH:
           k += 1
           if k > 100:
               break
       if k < 25:
           data.append(0)
       else:
           data.append(1)

       j += 1


  humidity_bit = data[0:8]
  humidity_point_bit = data[8:16]
  temperature_bit = data[16:24]
  temperature_point_bit = data[24:32]
  check_bit = data[32:40]

  global humidity
  global temperature
  global check
  humidity_point = 0
  temperature_point = 0
  check = 0
  temperature = 0
  humidity = 0

  for i in range(8):
       humidity += humidity_bit[i] * 2 ** (7 - i)
       humidity_point += humidity_point_bit[i] * 2 ** (7 - i)
       temperature += temperature_bit[i] * 2 ** (7 - i)
       temperature_point += temperature_point_bit[i] * 2 ** (7 - i)
       check += check_bit[i] * 2 ** (7 - i)

  global tmp
  tmp = humidity + humidity_point + temperature + temperature_point
  GPIO.cleanup()
  return temperature, humidity

def get_temp():

  x, y = DHT11()
  while check != tmp or tmp == 0:
    x, y = DHT11()
  return x, y
