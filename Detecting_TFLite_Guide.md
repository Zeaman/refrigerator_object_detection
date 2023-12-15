# How to Run TensorFlow Lite Models on Windows for detecting Refiregrator indoor materials using webcam
This guide shows how to set up a TensorFlow Lite Runtime environment on a Windows PC. We'll use [Anaconda](https://www.anaconda.com/) to create a Python environment to install the TFLite Runtime in. It's easy!

## Step 1. Download and Install Anaconda (use python 3.9)
First, install [Anaconda](https://www.anaconda.com/), which is a Python environment manager that greatly simplifies Python package management and deployment. Anaconda allows you to create Python virtual environments on your PC without interfering with existing installations of Python. Go to the [Anaconda Downloads page](https://www.anaconda.com/products/distribution) and click the Download button.

When the download finishes, open the downloaded .exe file and step through the installation wizard. Use the default install options.

## Step 2. Set Up Virtual Environment and Directory
Go to the Start Menu, search for "Anaconda Command Prompt", and click it to open up a command terminal. We'll create a folder called `webcam_detect` directly in the C: drive. Notice: You can use any other folder location you like, just make sure to modify the commands below to use the correct file paths. Create the folder and move into it by issuing the following commands in the terminal:

```
mkdir C:\webcam_detect
cd C:\webcam_detect
```

Next, create a Python 3.9 virtual environment by issuing:

```
conda create --name tflite1-env python=3.9
```

Enter "y" when it asks if you want to proceed. Activate the environment and install the required packages by issuing the commands below. We'll install TensorFlow, OpenCV, and a downgraded version of protobuf. TensorFlow is a pretty big download (about 450MB), so it will take a while.

```
conda activate tflite1-env
pip install tensorflow opencv-python protobuf==3.20.*
```

Download the detection scripts from this repository by issuing:

```
curl https://github.com/Zeaman/refrigerator_object_detection/blob/main/TFLite_detection_image.py --output TFLite_detection_image.py
curl https://github.com/Zeaman/refrigerator_object_detection/blob/main/TFLite_detection_video.py --output TFLite_detection_video.py
curl https://github.com/Zeaman/refrigerator_object_detection/blob/main/TFLite_detection_webcam.py --output TFLite_detection_webcam.py
curl https://github.com/Zeaman/refrigerator_object_detection/blob/main/TFLite_detection_stream.py --output TFLite_detection_stream.py
```

## Step 3. Move TFLite Model into Directory
Next, take the custom TFLite model that was trained and downloaded from the Colab notebook and move it into the C:\tflite1 directory. It should be in a file called `custom_model_lite.zip`. Move that file to the C:\tflite1 directory, use:

Navigate to Source Directory:
```
cd /path/to/source_directory
```

Copy the File:
```
cp custom_model_lite.zip /path/to/destination_directory
```

Navigate to Destination Directory:
```
cd /path/to/destination_directory
```
Paste the File('custom_model_lite.zip'):
```
mv custom_model_lite.zip .
```

Once it's moved, unzip it using:
```
tar -xf custom_model_lite.zip
```

At this point, you should have a folder at C:\webcam_detect\custom_model_lite which contains at least a `detect.tflite` and `labelmap.txt` file.

## Step 4. Run TensorFlow Lite Model!
Run the TFLite model is next task. Call one of the detection scripts and point it at your model folder with the `--modeldir` option. For example, to run your `custom_model_lite` model on a webcam, issue:

```
python TFLite_detection_webcam.py --modeldir=custom_model_lite
```

A window will appear showing detection results drawn on the live webcam feed. 
