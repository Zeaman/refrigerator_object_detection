# refrigerator_object_detection
Overview
This repository implements indoor fridge object detection using two powerful models: TensorFlow Lite and YOLOv8 (PyTorch). The models are trained and saved in their respective formats for seamless integration into various applications.

Models and Weights
TensorFlow Lite Model:

The TensorFlow Lite model is optimized for efficient deployment on mobile and edge devices. The model is saved in the TFLite format.
YOLOv8 Model (PyTorch):

The YOLOv8 model, based on PyTorch, is renowned for its accuracy and versatility. Three different weights, named weight1, weight2, and weight3, are provided, each representing a distinct training attempt using the best.pt model.
Testing the Models
Using the best.pt YOLOv8 model, we have conducted comprehensive testing across multiple scenarios:

Images:

The model demonstrates robust object detection when applied to static images.
Video Feed:

Real-time object detection is achieved when processing video feeds, showcasing the model's efficiency in dynamic environments.
Live Webcam Feed:

The YOLOv8 model excels in live webcam feed scenarios, ensuring reliable performance for interactive applications.
Flask API Integration
The repository includes a Flask API for seamless integration into web applications. The API allows testing the models using a local IP address, providing a convenient way to evaluate their effectiveness in a practical environment.

Usage
To get started, follow the instructions in the respective folders for TensorFlow Lite and YOLOv8. Detailed guidance on model usage, testing, and Flask API integration is provided in each section.

Feel free to explore the code, contribute, and adapt the models to your specific requirements.

Happy coding!
