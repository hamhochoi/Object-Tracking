## Overview
- This project combines multiple repos into one to do multiple car tracking tasks. These tasks are likely faced in autonomous driving vehicle problem.

## This project contains
- Car Tracking
	- Object Detector: Yolov4
	- Tracking: DeepSORT (includes Kalman Filter + Hungarian)
- Car Counting
- Speed Estimation (using real world coordination)
- Tracking real world coordination of objects using map() in yolov4-deepsort-master/utils/map_location.py (4 hand coded coordinates must be provided first). ![see more](./yolov4-deepsort-master/README_hamhochoi.md)
- Lane Segmentation

## Pretrained files
- Car Detection: Copy and paste yolov4.weights from your downloads folder into the 'data' folder of this repository.
	- Yolov4: https://drive.google.com/file/d/1cewMfusmPjYWbrnuJRuKhPMwRe_b9PaT/view
	- Yolov4-tiny: https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4-tiny.weights
- Lane Segmentation: https://drive.google.com/drive/folders/14TtrNFY94FS1fIDspzg4ZRPCFT5OXujc
	- create 'model' folder and put all pretrained files in there.
	
## How to run
- Car tracking + counting + speed estimation: 
```
		cd yolov4-deepsort-master
		python object_tracker.py --video ./data/video/highway9.mp4 --output ./outputs/highway9.avi --model yolov4
```	
- The results will be stored in 'outputs' folder.
	
- Lane Segmentation: Apply lane segmentation into results of car tracking phase as follow
	- Copy images from 'yolov4-deepsort-master/outputs/frame/\*' to 'LaneSegmentationNetwork/data/image/image'
	- Run lane segmentation:
	```
			python prediction.py
	```
- The results are LaneSegmentationNetwork/*.avi

## Demo
![demo](./demo.gif)


## Reference
- https://github.com/theAIGuysCode/yolov4-deepsort
- https://github.com/Smorodov/Multitarget-tracker
- https://medium.com/hal24k-techblog/how-to-track-objects-in-the-real-world-with-tensorflow-sort-and-opencv-a64d9564ccb1
