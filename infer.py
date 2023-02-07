from ultralytics import YOLO
import yaml
import cv2
import os
import shutil
cwd = os.getcwd()
model = YOLO(r"C:\Users\Shobh\Desktop\InterIIT\best.pt")

vid = cv2.VideoCapture(0)
data = []
moves = []  
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
            ax = "Move Right"
            moves.append("R")
            # change x axis parameter to move right
        if xc<0.45 :
            ax = "Move Left"
            moves.append("L")
            # change x axis parameter to move left
        if yc>0.55 :
            ay = "Move Up"
            moves.append("U")
            # change y axis parameter to move up
        if yc<0.45 :
            ay = 'Move Down'
            moves.append("D")
            # change y axis parameter to move down
        if xc<0.55 and xc>0.45 and yc<0.55 and yc>0.45 and nh<0.8:
            az = "Move Forward"
            moves.append("F")
            # change y axis parameter to move forward
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
open("data.txt", "a").write("\n".join(("\t".join(item)) for item in moves))