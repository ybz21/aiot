import face_recognition
import cv2
import numpy as np
import os
import time
import csv

current_path = os.path.dirname(os.path.abspath(__file__))

UN_KNOWN = 'Unknown'
FACE_THRESHOLD = 0.44
TIME_THRESHOLD = 30


CAMERA_NO = 1


def init_faces():
    faces_dir = os.path.join(current_path, 'face_models')
    files = os.listdir(faces_dir)

    known_face_encodings = []
    known_face_names = []

    for face_pic in files:
        name = face_pic.split('.')[0]
        path = os.path.join(faces_dir, face_pic)
        print(f'load person: {name}')

        temp_image = face_recognition.load_image_file(path)
        temp_face_encoding = face_recognition.face_encodings(temp_image)[0]

        known_face_encodings.append(temp_face_encoding)
        known_face_names.append(name)
    return known_face_names, known_face_encodings


def detect(known_face_names, known_face_encodings, threshold=FACE_THRESHOLD):
    last_face_time = time.time()
    last_face_name = UN_KNOWN

    video_capture = cv2.VideoCapture(CAMERA_NO)

    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    while True:
        ret, frame = video_capture.read()
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Only process every other frame of video to save time
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            if len(face_encodings) != 1:
                local_time = time.strftime("%Y-%m-%d %H:%M:%S")
                print(f'{local_time}, person num: {len(face_encodings)}, skip this situation!')
                time.sleep(1)
                continue

            # face_name = ''
            # for face_encoding in face_encodings:
            face_encoding = face_encodings[0]
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            face_name = UN_KNOWN

            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)

            if face_distances[best_match_index] < threshold and matches[best_match_index]:
                face_name = known_face_names[best_match_index]
            else:
                continue

            time_now = time.time()
            if face_name != last_face_name or time_now - last_face_time > TIME_THRESHOLD:
                face_names = [face_name]
                pic_name = f'{time_now}_{face_name}.jpg'
                print(f'detect person: {face_name}')
                save_pic(frame, face_locations, face_names, pic_name)
                write_csv(face_name, time_now, pic_name)

                last_face_name = face_name
                last_face_time = time_now
            else:
                continue

        process_this_frame = not process_this_frame


def save_pic(frame, face_locations, face_names, pic_name):
    print(f'save pic:{pic_name}')
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    pic_path = os.path.join(current_path, 'results', pic_name)
    cv2.imwrite(pic_path, frame)


def write_csv(name, time_now, pic_name):
    path = os.path.join(current_path, 'results', 'face.csv')
    format = '%Y-%m-%d %H:%M:%S'
    time_tuple = time.localtime(time_now)
    result = time.strftime(format, time_tuple)

    with open(path, 'a+') as f:
        csv_write = csv.writer(f)
        data_row = [name, result, pic_name]
        csv_write.writerow(data_row)


def main():
    known_face_names, known_face_encodings = init_faces()
    detect(known_face_names, known_face_encodings)


if __name__ == '__main__':
    main()
