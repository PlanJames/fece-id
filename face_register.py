import cv2 as cv
import mediapipe as mp
from imutils.video import VideoStream
import imutils

class FaceRegister:
    def __init__(self, username):
        self.username = username
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, min_detection_confidence=0.5)
        self.drawing_spec = mp.solutions.drawing_utils.DrawingSpec(thickness=1, circle_radius=1)
        self.cap = VideoStream(src=0).start()
        self.run()

    def run(self):
        while True:
            frame = self.cap.read()
            frame = imutils.resize(frame, width=400)
            rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            results = self.face_mesh.process(rgb_frame)

            if results.multi_face_landmarks:
                for face_landmarks in results.multi_face_landmarks:
                    mp.solutions.drawing_utils.draw_landmarks(
                        image=frame,
                        landmark_list=face_landmarks,
                        connections=self.mp_face_mesh.FACEMESH_CONTOURS,  # Use FACEMESH_CONTOURS for fewer points
                        landmark_drawing_spec=self.drawing_spec,
                        connection_drawing_spec=self.drawing_spec)

            cv.imshow('Face ID', frame)

            key = cv.waitKey(1) & 0xFF
            if key == ord(' '):  # Press space to capture
                if results.multi_face_landmarks:
                    face_landmarks = results.multi_face_landmarks[0]
                    # Save the face landmarks or the frame as needed
                    break
            elif key == ord('q') or cv.getWindowProperty('Face ID', cv.WND_PROP_VISIBLE) < 1:  # Press 'q' to exit or close window
                break

        self.cap.stop()
        cv.destroyAllWindows()

if __name__ == "__main__":
    FaceRegister("test_user")