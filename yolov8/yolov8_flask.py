# Install Flask on your system by writing
# 1. Activate the VENV (if created)
# 2. Install flask: !pip install Flask

#Import requiered dependencies
import cv2
from flask import Flask, Response,jsonify,request


# Video Detection is the Function which performs Object Detection on Input Video used from: 'predict_yolov8_video'
from YOLO_FLASK import video_detection

# Intializeing the Flask:
app = Flask(__name__)

app.config['SECRET_KEY'] = 'zeaman44' # 'zeaman44' is a key that you can change
#Generate_frames function takes path of input video file and  gives us the output with bounding boxes around detected objects

#Now we will display the output video with detection
def generate_frames(path_x = ''):
    # yolo_output variable stores the output for each detection
    # the output with bounding box around detected objects

    yolo_output = video_detection(path_x)
    for detection_ in yolo_output:
        ref,buffer=cv2.imencode('.jpg',detection_)
        #We will display the individual frames using 'Yield keyword':
        frame=buffer.tobytes()
        yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame +b'\r\n')

# For vidoes uploaded
@app.route('/video')
def video():
    return Response(generate_frames(path_x='C:/My_Files/UpWork_jobs/refrigerator_object_detection_YOLOv8/test_videos/test1.mp4'), mimetype='multipart/x-mixed-replace; boundary=frame')
    #return Response(generate_frames(path_x=0), mimetype='multipart/x-mixed-replace; boundary=frame')

# For live webcam feed
@app.route('/webcam')
def webcam():
    return Response(generate_frames(path_x=0), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)