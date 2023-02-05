from ultralytics import YOLO
import yaml
import cv2
import os
import shutil
cwd = os.getcwd()
model = YOLO(r"C:\Users\Shobh\Desktop\InterIIT\best.pt")

vid = cv2.VideoCapture(0)
data = []  
while(True):
      
    ret, frame = vid.read()
    model.predict(frame,save_txt=True)
    path = cwd+r"\runs\detect\predict\labels\image0.txt"
    if os.path.exists(path):
        lis = open(path, "r").readlines()
        li = lis[-1].split()
        xc,yc,nw,nh = float(li[1]), float(li[2]), float(li[3]), float(li[4])
        data = [xc,yc,nw,nh]
        ax = ""
        ay = ""
        az = ""
        if xc>0.55 :
            ax = "Move Rightq"
        if xc<0.45 :
            ax = "Move Left"
        if yc>0.55 :
            ay = "Move Up"
        if yc<0.45 :
            ay = 'Move Down'
        if xc<0.55 and xc>0.45 and yc<0.55 and yc>0.45 and nh<0.8:
            az = "Move Forward"
        print(ax,ay,az)
    dir = cwd+"\\runs\\detect\\predict"
    if os.path.exists(dir):
        shutil.rmtree(dir)
    #cv2.imshow('frame', frame)
    #if cv2.waitKey(1) & 0xFF == ord('q'):
    break
vid.release()
cv2.destroyAllWindows()
print(data)