import face_recognition
import cv2
import numpy as np
import os
import time

current_path = os.path.dirname(os.path.abspath(__file__))


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


def detect(known_face_names, known_face_encodings, threshold=0.44):
    video_capture = cv2.VideoCapture(1)

    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    while True:

        # Grab a single frame of video
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

            face_names = []

            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"

                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)

                if face_distances[best_match_index] < threshold and matches[best_match_index]:
                    name = known_face_names[best_match_index]

                face_names.append(name)

        process_this_frame = not process_this_frame

        # Display the results
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
        cv2.imshow('Video', frame)

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()


def main():
    known_face_names, known_face_encodings = init_faces()
    detect(known_face_names, known_face_encodings)


if __name__ == '__main__':
    main()
