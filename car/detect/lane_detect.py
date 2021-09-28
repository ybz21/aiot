import numpy as np
import cv2
import matplotlib.pyplot as plt
import time


def canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('./image/gray.jpg', gray)

    blur = cv2.GaussianBlur(gray, (17, 17), 0)
    cv2.imwrite('./image/blur.jpg', blur)

    ret, binary = cv2.threshold(blur, 180, 255, cv2.THRESH_BINARY)
    cv2.imwrite('./image/binary.jpg', binary)

    can = cv2.Canny(binary, 50, 150)
    cv2.imwrite('./image/canny.jpg', can)

    plt.imshow(can)
    plt.show()


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
    img = cv2.imread('./image/a_test.jpeg')
    lane_image = np.copy(img)

    can = canny(lane_image)

    roi = region_of_interest(can)

    hough = hough_transform(roi)



if __name__ == '__main__':
    main()
