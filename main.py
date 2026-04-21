import cv2
import mediapipe as mp

# IMPORT YOUR MODULES
from utils import calculate_angle
from tracker import log_workout

# ---------------- MediaPipe Setup ----------------
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

# ---------------- System Variables ----------------
exercise_mode = "squat"
counter = 0
stage = None
running = False

# ---------------- Main Loop ----------------
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = pose.process(rgb)

    # ---------------- UI TEXT ----------------
    cv2.putText(frame, "S=Start  P=Pause  Q=Quit  1=Squat  2=Pushup  3=Lunge",
                (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)

    cv2.putText(frame, f"Mode: {exercise_mode}", (10, 55),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,255), 2)

    cv2.putText(frame, f"Reps: {counter}", (10, 85),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)

    # ---------------- Pose Processing ----------------
    if running and results.pose_landmarks:
        mp_draw.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        landmarks = results.pose_landmarks.landmark

        # ================= SQUAT =================
        if exercise_mode == "squat":

            hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                   landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]

            knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
                    landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]

            ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
                     landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]

            angle = calculate_angle(hip, knee, ankle)

            if angle < 70:
                stage = "down"

            if angle > 160 and stage == "down":
                stage = "up"
                counter += 1
                log_workout("squat", counter)

        # ================= PUSHUP =================
        elif exercise_mode == "pushup":

            shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                        landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]

            elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                     landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]

            wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                     landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

            angle = calculate_angle(shoulder, elbow, wrist)

            if angle < 90:
                stage = "down"

            if angle > 160 and stage == "down":
                stage = "up"
                counter += 1
                log_workout("pushup", counter)

        # ================= LUNGE =================
        elif exercise_mode == "lunge":

            hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                   landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]

            knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
                    landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]

            ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
                     landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]

            angle = calculate_angle(hip, knee, ankle)

            if angle < 90:
                stage = "down"

            if angle > 160 and stage == "down":
                stage = "up"
                counter += 1
                log_workout("lunge", counter)

    # ---------------- Show Frame ----------------
    cv2.imshow("AI Fitness Analyzer", frame)

    # ---------------- Controls ----------------
    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):
        running = True

    elif key == ord('p'):
        running = False

    elif key == ord('q'):
        break

    elif key == ord('1'):
        exercise_mode = "squat"
        counter = 0

    elif key == ord('2'):
        exercise_mode = "pushup"
        counter = 0

    elif key == ord('3'):
        exercise_mode = "lunge"
        counter = 0


cap.release()
cv2.destroyAllWindows()