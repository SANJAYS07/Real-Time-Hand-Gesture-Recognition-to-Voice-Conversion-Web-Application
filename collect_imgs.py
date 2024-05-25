import os
import cv2

DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes =60
dataset_size = 25

cap = cv2.VideoCapture(0)  # Use 0 instead of 2 if you have only one camera

for j in range(3):
    if not os.path.exists(os.path.join(DATA_DIR, str(j+number_of_classes))):
        os.makedirs(os.path.join(DATA_DIR, str(j+number_of_classes)))

    print('Collecting data for class {}'.format(j+number_of_classes))

    done = False
    while True:
        ret, frame = cap.read()
        cv2.putText(frame, 'Ready? Press "Q" ! :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3,
                    cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) == ord('q'):
            break

    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        if not ret or frame.shape[0] == 0 or frame.shape[1] == 0:
            print("Error: Couldn't read frame from the camera or invalid frame dimensions")
            break

        cv2.imshow('frame', frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(DATA_DIR, str(j+number_of_classes), '{}.jpg'.format(counter)), frame)

        counter += 1

cap.release()
cv2.destroyAllWindows()
