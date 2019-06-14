# Lane-Detector-Node
ROS Node to detect lane using deep learning models. The node can also be used to apply lane detection over a video.

## Usage
### Requirements
1. tensorflow=1.13
2. opencv > 3.0

### Installation
```
cd catkin_ws # name of your workspace
cd src
git clone https://github.com/sumitbinnani/Lane-Detector-Node.git lane-detector
cd ..
catkin_make
```

### Subscribing to a node
```
rosrun lane-detector lane-detector.py --model <model_name> \
      --subscriber node --name <path to file>
```

### Playing over a video
```
rosrun lane-detector lane-detector.py --model <model_name> \
     --subscriber video --name <subscriber>
```

## Other Details
The `y_range` parameter is used to decide the area in the image to localize the lane.
The pre-trained models are placed at `detectors/pretrained-models` and can be replaced
by another trained models.

# To Do
- [ ] Add lane tracking
- [ ] Add more details about model training and freezing weights
