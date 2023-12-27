# Randomly splits images to 80% train, 10% validation, and 10% test, and moves them to their respective folders.


import glob
from pathlib import Path
import random
import os
import shutil

# Define paths to image folders
image_path = 'C:/My_Files/UpWork_jobs/refrigerator_object_detection_YOLOv8/dataset'
train_path = 'C:/My_Files/UpWork_jobs/refrigerator_object_detection_YOLOv8/refrigerator_dataset/train/images'
val_path = 'C:/My_Files/UpWork_jobs/refrigerator_object_detection_YOLOv8/refrigerator_dataset/valid/images'
test_path = 'C:/My_Files/UpWork_jobs/refrigerator_object_detection_YOLOv8/refrigerator_dataset/test/images'

# Get list of all images
jpg_file_list = list(Path(image_path).rglob('*.jpg')) + list(Path(image_path).rglob('*.JPG'))
png_file_list = list(Path(image_path).rglob('*.png'))
bmp_file_list = list(Path(image_path).rglob('*.bmp'))

file_list = jpg_file_list + png_file_list + bmp_file_list
file_num = len(file_list)
print('Total images: %d' % file_num)

# Determine number of files to move to each folder
train_percent = 0.8  # 80% of the files go to train
val_percent = 0.1  # 10% go to validation
test_percent = 0.1  # 10% go to test
train_num = int(file_num * train_percent)
val_num = int(file_num * val_percent)
test_num = file_num - train_num - val_num
print('Images moving to train: %d' % train_num)
print('Images moving to validation: %d' % val_num)
print('Images moving to test: %d' % test_num)

# Select and move files to train folder
for i in range(train_num):
    move_me = random.choice(file_list)
    fn = move_me.name
    base_fn = move_me.stem  # Define 'base_fn' within the loop
    parent_path = move_me.parent  # Define 'parent_path' within the loop
    xml_fn = base_fn + '.xml'
    shutil.move(str(move_me), os.path.join(train_path, fn))  # Use str() to convert Path to string
    shutil.move(os.path.join(str(parent_path), xml_fn), os.path.join(train_path, xml_fn))
    file_list.remove(move_me)

# Select and move files to validation folder
for i in range(val_num):
    move_me = random.choice(file_list)
    fn = move_me.name
    base_fn = move_me.stem  # Define 'base_fn' within the loop
    parent_path = move_me.parent  # Define 'parent_path' within the loop
    xml_fn = base_fn + '.xml'
    shutil.move(str(move_me), os.path.join(val_path, fn))  # Use str() to convert Path to string
    shutil.move(os.path.join(str(parent_path), xml_fn), os.path.join(val_path, xml_fn))
    file_list.remove(move_me)

# Move remaining files to test folder
for i in range(test_num):
    move_me = random.choice(file_list)
    fn = move_me.name
    base_fn = move_me.stem  # Define 'base_fn' within the loop
    parent_path = move_me.parent  # Define 'parent_path' within the loop
    xml_fn = base_fn + '.xml'
    shutil.move(str(move_me), os.path.join(test_path, fn))  # Use str() to convert Path to string
    shutil.move(os.path.join(str(parent_path), xml_fn), os.path.join(test_path, xml_fn))
    file_list.remove(move_me)

