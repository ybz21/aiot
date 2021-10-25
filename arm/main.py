# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time         : 2021/10/24 1:41 下午
# @Author       : yanbingzheng@4paradigm.com
# @File         : main.py
# @Description  : xxxxx
import Jetson.GPIO as GPIO
import time
import signal
import atexit

atexit.register(GPIO.cleanup)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(32, GPIO.OUT, initial=False)
p = GPIO.PWM(32, 50)  # 50HZ
p.start(0)
time.sleep(2)

while (True):
    for i in range(0, 181, 10):
        p.ChangeDutyCycle(2.5 + 10 * i / 180)  # 设置转动角度
        time.sleep(0.02)  # 等该20ms周期结束
        p.ChangeDutyCycle(0)  # 归零信号
        # time.sleep(0.2)

    time.sleep(1)

    for i in range(181, 0, -10):
        p.ChangeDutyCycle(2.5 + 10 * i / 180)
        time.sleep(0.02)
        p.ChangeDutyCycle(0)
