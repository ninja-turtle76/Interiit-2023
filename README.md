# Anveshan
Anveshan is our approach to make charging of Electric Vehicles autonomous at specialized charging stations.

This repository contains the code that makes the functioning of the detection model used in the robot to successfully recognise and approach the charging port possible.

**YOLOv8 Model Trainer.ipynb**

This is the python notebook that was used to train the detection model using a Yolov8 architecture on a dataset prepared using Roboflow.

**best.pt**

This file contains the weights of the best model that was trained using the model trainer code

**infer.py**

This is the python program that is initially used to detect the location of the charging port and help the robot approach it by passing commands to the development board.

**aim.py**

This is the python program that is run when the end affector has reached the charging port and is responsible for the aiming phase where the plugging operation takes place.

**aim.m and interiit.m**

These two files can be used to run the python scripts in a MATLAB environment.

**requirements.txt**

Before running any of the above programs, the packages mentioned in this file must be installed.
