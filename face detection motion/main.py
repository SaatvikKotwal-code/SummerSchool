import cv2
import mediapipe as mp
from fer import FER
fer = FER()


# Initialize mediapipe solutions
mp_face_mesh = mp.solutions.face_mesh
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Initialize FER detector
detector = FER(mtcnn=True)

# Initialize webcam
cap = cv2.VideoCapture(0)

# Face Mesh and Hands setup
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, min_detection_confidence=0.5)
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)

print("[INFO] Starting Emotion-based Color Detection. Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert BGR to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Default color (grey)
    overlay_color = (200, 200, 200)

    # Emotion detection using FER
    emotions = detector.detect_emotions(frame)
    for result in emotions:
        (x, y, w, h) = result['box']
        emotion_scores = result['emotions']
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

        # Filter only Angry, Happy, Neutral and set overlay color accordingly
        if dominant_emotion == 'angry':
            label = 'Angry'
            overlay_color = (0, 0, 255)  # Red
        elif dominant_emotion == 'happy':
            label = 'Happy'
            overlay_color = (0, 255, 0)  # Green
        elif dominant_emotion == 'neutral':
            label = 'Moderate'
            overlay_color = (255, 0, 0)  # Blue
        else:
            label = 'Other'
            overlay_color = (200, 200, 200)  # Grey

        # Draw bounding box and emotion label
        cv2.rectangle(frame, (x, y), (x+w, y+h), overlay_color, 2)
        cv2.putText(frame, label, (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, overlay_color, 2)

    # Process face landmarks with overlay color
    face_results = face_mesh.process(rgb_frame)
    if face_results.multi_face_landmarks:
        for face_landmarks in face_results.multi_face_landmarks:
            mp_drawing.draw_landmarks(
                frame,
                face_landmarks,
                mp_face_mesh.FACEMESH_TESSELATION,
                landmark_drawing_spec=None,
                connection_drawing_spec=mp_drawing.DrawingSpec(color=overlay_color, thickness=1, circle_radius=1)
            )

    # Process hand landmarks with overlay color
    hand_results = hands.process(rgb_frame)
    if hand_results.multi_hand_landmarks:
        for hand_landmarks in hand_results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing.DrawingSpec(color=overlay_color, thickness=2, circle_radius=2),
                mp_drawing.DrawingSpec(color=overlay_color, thickness=2)
            )

    # Display output
    cv2.imshow("Emotion-based Color Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
