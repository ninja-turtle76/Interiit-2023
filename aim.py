from ultralytics import YOLO
import yaml
import cv2
import os
import shutil
cwd = os.getcwd()
model = YOLO(r"C:\Users\Shobh\Desktop\InterIIT\best.pt")
last = 'left'
last_r = 0

def plug():
    print("Plug in the charger")
    # change z axis parameter to plug in charger 
    return

def move(dir):
    if dir == 'left':
        print("Rotate left")
        # change parameter to rotate end effector
        return
    else:
        print("Rotate Right")
        # change parameter to rotate end effector
        return

def aim(last,r):
    if last == 'right' and last_r>r:
        last = 'left'
    elif last == 'left' and last_r>r:
        last = 'right'
    move(last)
    return

vid = cv2.VideoCapture(0)
data = []  
count=0
while(True):
      
    ret, frame = vid.read()
    model.predict(frame,save_txt=True)
    path = cwd+r"\runs\detect\predict\labels\image0.txt"
    if os.path.exists(path):
        lis = open(path, "r").readlines()
        li = lis[-1].split()
        xc,yc,nw,nh = float(li[1]), float(li[2]), float(li[3]), float(li[4])
        data = [xc,yc,nw,nh]
        if count==5:
            plug()
        if nw/nh < 0.652:
            aim(last,nw/nh)
            last_r = nw/nh
            count=0
        else:
            count=count+1
    dir = cwd+"\\runs\\detect\\predict"
    if os.path.exists(dir):
        shutil.rmtree(dir)
    #cv2.imshow('frame', frame)
    #if cv2.waitKey(1000) & 0xFF == ord('q'):
    break
vid.release()
cv2.destroyAllWindows()
print(data)