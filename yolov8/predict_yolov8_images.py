import cv2
import math
from ultralytics import YOLO



# Load the trained best model:
model = YOLO("C:/My_Files/UpWork_jobs/refrigerator_object_detection_YOLOv8/result/result_one/weights1/best.pt")

# Define the 29 classes
classNames = ['apple', 'avocado', 'banana', 'beef_mince', 'beetroot', 'bellpepper', 'beverage', 
               'cabbage', 'carrot', 'cauliflower', 'chicken_thighs', 'cucumber', 'dairy', 'egg', 'eggplant',
               'grapes', 'iceCream', 'jalepeno', 'lemon', 'mango', 'meat', 'mutton', 'orange', 'peas', 
               'pineapple', 'steak', 'strawberry', 'tomato', 'watermelon']


# Use the model to detect:
model_detects = model('C:/My_Files/UpWork_jobs/refrigerator_object_detection_YOLOv8/test_images/2.jpeg', show=True)
key = cv2.waitKey(0) & 0xFF  # Wait indefinitely for a key press
if key == ord('q') or key == ord('Q'):  # Check if pressed key is 'q' or 'Q'
    cv2.destroyAllWindows()  # Close all OpenCV windows
