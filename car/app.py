import cv2
import time
import threading
from flask import Response, Flask
import nanocamera as nano

# Image frame sent to the Flask object
global video_frame
video_frame = None


# Use locks for thread-safe viewing of frames in multiple browsers
global thread_lock
thread_lock = threading.Lock()

# Create the Flask object for the application
app = Flask(__name__)

camera = nano.Camera(flip=0, width=1280, height=720, fps=1)
print('CSI Camera is now ready')

def captureFrames():
    global video_frame, thread_lock
    while True:
        try:
            frame = camera.read()
            cv2.imwrite('./bb.jpg',frame)
            print(frame)
            with thread_lock:
                video_frame = frame.copy()

            key = cv2.waitKey(30) & 0xff
            if key == 27:
                break

        except KeyboardInterrupt:
            break

    camera.release()


def encodeFrame():
    global thread_lock
    while True:
        # Acquire thread_lock to access the global video_frame object
        with thread_lock:
            global video_frame
            if video_frame is None:
                continue
            return_key, encoded_image = cv2.imencode(".jpg", video_frame)
            if not return_key:
                continue

        # Output image as a byte array
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' +
               bytearray(encoded_image) + b'\r\n')


@app.route("/")
def streamFrames():
    return Response(encodeFrame(), mimetype="multipart/x-mixed-replace; boundary=frame")


# check to see if this is the main thread of execution
if __name__ == '__main__':
    # Create a thread and attach the method that captures the image frames, to it
    process_thread = threading.Thread(target=captureFrames)
    process_thread.daemon = True

    # Start the thread
    process_thread.start()

    # start the Flask Web Application
    # While it can be run on any feasible IP, IP = 0.0.0.0 renders the web app on
    # the host machine's localhost and is discoverable by other machines on the same network
    app.run("0.0.0.0", port="8000")
