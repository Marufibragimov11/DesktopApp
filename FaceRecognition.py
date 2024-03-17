import cv2
import face_recognition


def recognize_face():
    model = "data/haarcascade_frontalface_default.xml"
    face_cascade = cv2.CascadeClassifier(model)

    known_images = ["data/my_photo.jpg", "data/smiling_man.jpg"]
    known_names = ["Maruf", "Steve"]

    known_encodings = []
    for image in known_images:
        img = cv2.imread(image)
        rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        faces = face_recognition.face_locations(rgb_img)

        for face in faces:
            encoding = face_recognition.face_encodings(rgb_img, [face])[0]
            known_encodings.append(encoding)

    video_capture = cv2.VideoCapture(0)

    while True:
        ret, frame = video_capture.read()

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        faces = face_cascade.detectMultiScale(rgb_frame, 1.1, 4)

        for (x, y, w, h) in faces:
            roi = rgb_frame[y:y + h, x:x + w]

            face_locations = face_recognition.face_locations(roi)
            if len(face_locations) == 0:
                continue

            encoding = face_recognition.face_encodings(roi)[0]

            matches = face_recognition.compare_faces(known_encodings, encoding)
            name = "Unknown"
            if True in matches:
                first_match_index = matches.index(True)
                name = known_names[first_match_index]

            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            cv2.putText(frame, name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)

        cv2.imshow('Face Recognition', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()


recognize_face()