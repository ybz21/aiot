import cv2
import numpy as np

path = '/Users/4paradigm/workspace/go/src/jetson/pic'
path = '/home/yanbingzheng/Pictures'


def save_photo():
    cap = cv2.VideoCapture(0)
    # cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 640)
    # cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 480)

    ret, frame = cap.read()
    cv2.imwrite(path + '/cap.jpg', frame)

    cap.release()


def save_video():
    cap = cv2.VideoCapture(0)  # 0代表摄像头编号，可以修改

    # define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    out = cv2.VideoWriter(path + '/output.avi', fourcc, 20.0, (640, 480))
    t = 0
    while (cap.isOpened()):
        t += 1
        ret, frame = cap.read()
        if ret == True:
            frame = cv2.flip(frame, 0)

            # write the flipped frame
            out.write(frame)
            # cv2.imshow('frame', frame)
            if t >= 1000:
                break
        else:
            break

    # release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()


save_photo()
