# import cv2
# import os

# # ==========================
# # Load Haar Cascade
# # ==========================
# cascade_file = "haarcascade_frontalface_default.xml"

# if not os.path.exists(cascade_file):
#     print(f"Error: {cascade_file} not found!")
#     exit()

# face_cascade = cv2.CascadeClassifier(cascade_file)

# if face_cascade.empty():
#     print("Error: Could not load Haar Cascade.")
#     exit()

# # ==========================
# # Open Camera
# # ==========================
# camera = None

# for index in [0, 1, 2]:
#     cap = cv2.VideoCapture(index, cv2.CAP_DSHOW)

#     if cap.isOpened():
#         ret, frame = cap.read()
#         if ret:
#             camera = cap
#             print(f"Camera opened successfully (Index: {index})")
#             break
#         else:
#             cap.release()

# if camera is None:
#     print("No working camera found!")
#     exit()

# camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
# camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# print("Press 'Q' to Exit")

# # ==========================
# # Main Loop
# # ==========================
# while True:

#     ret, frame = camera.read()

#     if not ret:
#         print("Failed to read frame.")
#         break

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     faces = face_cascade.detectMultiScale(
#         gray,
#         scaleFactor=1.1,
#         minNeighbors=5,
#         minSize=(50, 50)
#     )

#     for (x, y, w, h) in faces:

#         cv2.rectangle(
#             frame,
#             (x, y),
#             (x + w, y + h),
#             (0, 255, 0),
#             2
#         )

#         cv2.putText(
#             frame,
#             "Face",
#             (x, y - 10),
#             cv2.FONT_HERSHEY_SIMPLEX,
#             0.8,
#             (0, 255, 0),
#             2
#         )

#     cv2.imshow("Face Detection", frame)

#     key = cv2.waitKey(1)

#     if key == ord('q') or key == ord('Q'):
#         break

# camera.release()
# cv2.destroyAllWindows()



import cv2
import time
# যেহেতু xml ফাইলটি এখন একই ফোল্ডারে আছে, তাই সরাসরি নাম দিলেই কাজ করবে
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

if face_cascade.empty():
    print("এরর: এখনো ফাইলটি লোড হচ্ছে না! নিশ্চিত করুন xml ফাইলটি এবং পাইথন কোডটি একই ফোল্ডারে আছে।")
    exit()

# ওয়েবক্যাম চালু করুন (DirectShow সহ)
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)


print("ক্যামেরা চালু হয়েছে। বের হওয়ার জন্য কীবোর্ডের 'q' বাটন চাপুন।")

while True:
    ret, frame = cap.read()
    if not ret:
        print("ক্যামেরা থেকে ছবি পাওয়া যাচ্ছে না!")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray, 
        scaleFactor=1.1, 
        minNeighbors=5, 
        minSize=(30, 30)
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('Real-Time Face Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()