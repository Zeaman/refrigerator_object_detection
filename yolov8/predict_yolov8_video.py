import cv2
import math
from ultralytics import YOLO

cap = cv2.VideoCapture('C:/My_Files/UpWork_jobs/refrigerator_object_detection_YOLOv8/test_videos/test3.mp4')
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))

# Load the trained best model:
model=YOLO("C:/My_Files/UpWork_jobs/refrigerator_object_detection_YOLOv8/result/result_two/weights/best.pt")

# Define the 29 classes
classNames = ['apple', 'avocado', 'banana', 'beef_mince', 'beetroot', 'bellpepper', 'beverage', 
           'cabbage', 'carrot', 'cauliflower', 'chicken_thighs', 'cucumber', 'dairy', 'egg', 'eggplant',
           'grapes', 'iceCream', 'jalepeno', 'lemon', 'mango', 'meat', 'mutton', 'orange', 'peas', 
           'pineapple', 'steak', 'strawberry', 'tomato', 'watermelon']

while True:
    success, img = cap.read()

    # Doing detections using YOLOv8 frame by frame
    results = model(img, stream=True)

    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            print(x1, y1, x2, y2)

            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

            conf = math.ceil((box.conf[0] * 100)) / 100
            cls = int(box.cls[0])
            class_name = classNames[cls]
            label = f'{class_name}{conf}'

            t_size = cv2.getTextSize(label, 0, fontScale=1, thickness=2)[0]
            c2 = x1 + t_size[0], y1 - t_size[1] - 3
            cv2.rectangle(img, (x1, y1), c2, [255, 0, 255], -1, cv2.LINE_AA)
            cv2.putText(img, label, (x1, y1 - 2), 0, 1, [255, 255, 255], thickness=1, lineType=cv2.LINE_AA)

    out.write(img)
    cv2.imshow("Image", img)

    # Check for the 'q' or 'Q' key press to exit the loop
    if cv2.waitKey(1) & 0xFF in [ord('q'), ord('Q')]:
        break

out.release()
cv2.destroyAllWindows()  # Close the window when exiting the loop
cap.release()