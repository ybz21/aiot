# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time         : 2021/9/24 7:17 下午
# @Author       : yanbingzheng@4paradigm.com
# @File         : my.py
# @Description  : xxxxx
import numpy as np
import cv2
import matplotlib.pyplot as plt
import time


def canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('./gray.jpg', gray)

    blur = cv2.GaussianBlur(gray, (17, 17), 0)
    cv2.imwrite('./blur.jpg', blur)

    ret, binary = cv2.threshold(blur, 180, 255, cv2.THRESH_BINARY)
    cv2.imwrite('./binary.jpg', binary)

    can = cv2.Canny(binary, 50, 150)
    cv2.imwrite('./canny.jpg', can)

    plt.imshow(can)
    plt.show()


def region_of_interest(image):
    height = image.shape[0]
    # triangle = np.array([0, he])


def main():
    img = cv2.imread('./test.jpeg')
    lane_image = np.copy(img)

    can = canny(lane_image)

    # plt.imshow(gray)
    # cv2.imshow('img', img)
    # cv2.imshow('lane_image', lane_image)
    # cv2.imshow('gray', gray)
    # cv2.imshow('blur', blur)
    # cv2.waitKey(20 * 1000)


if __name__ == '__main__':
    main()
