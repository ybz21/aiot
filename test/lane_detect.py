import numpy as np
import cv2
import matplotlib.pyplot as plt
import time


def canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('./result/gray.jpg', gray)

    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    cv2.imwrite('./result/blur.jpg', blur)
    plt.imshow(blur)
    plt.show()

    ret, binary1 = cv2.threshold(blur, 100, 255, cv2.cv2.THRESH_BINARY_INV)
    cv2.imwrite('./result/binary1.jpg', binary1)
    plt.imshow(binary1)

    ret, binary2 = cv2.threshold(binary1, 100, 255, cv2.THRESH_BINARY)
    cv2.imwrite('./result/binary2.jpg', binary2)
    plt.imshow(binary2)
    plt.show()

    # can = cv2.Canny(binary, 50, 150)
    # cv2.imwrite('./result/canny.jpg', can)

    # plt.imshow(can)
    # plt.show()


def region_of_interest(image):
    return image


def hough_transform(image):
    rho = 1
    theta = np.pi / 180
    threshold = 15
    min_line_len = 40
    max_line_gap = 20
    lines = cv2.HoughLinesP(image, rho, theta, threshold, minLineLength=min_line_len, maxLineGap=max_line_gap)

    print(f'lines: {lines}')

    # cv2.imwrite('./image/hough.jpg', lines)
    return lines


def main():
    img = cv2.imread('./image_real/bb.jpg')
    lane_image = np.copy(img)

    can = canny(lane_image)

    roi = region_of_interest(can)

    hough = hough_transform(roi)



if __name__ == '__main__':
    main()
