import cv2

def authenticate_face():
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    cap = cv2.VideoCapture(0)

    print("Authenticating face... Press Q to exit")

    authenticated = False

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )
            authenticated = True

        cv2.imshow("Face Authentication", frame)

        if authenticated:
            print("Face detected. Access granted.")
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    return authenticated
