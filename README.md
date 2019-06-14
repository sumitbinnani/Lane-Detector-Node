# Lane-Detector-Node
ROS Node to detect lane using deep learning models. The node can also be used to apply lane detection over a video.

## Usage

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
rosrun lane-detector lane-detector.py --model <model_name>
     --subscriber video --name <subscriber>
```

## Other Details
Requirements:
1. tensorflow=1.13
2. opencv > 3.0

The pre-trained models can be replaced at the path `detectors/pretrained-models`. 
