# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 18:34:00 2020

@author: parneet
"""
import cv2
import sys
import mimetypes
inp = sys.argv[1]
mimestart = mimetypes.guess_type(inp)
try:
    mimestart == 'video'
except:
    print("\nUnsupported Format\n")
try:
    p = open(inp)
except :
    print('Error!! File not found')
    exit()
vidObj = cv2.VideoCapture(inp)
fps= vidObj.get(cv2.CAP_PROP_FPS)
#print(fps)
count=0

success=1

while success:
    success,image= vidObj.read()
    
    if(success == False and image == None):
        pass
    else:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
        cv2.imwrite("frame%d.jpg" % count, gray)
        count += 1


output_video_name="video_output.mp4"

fourcc = cv2.VideoWriter_fourcc(*'mp4v')

frame_per_second = fps

img = cv2.imread("frame0.jpg")
height,width,layers = img.shape
size = (width,height)
#print(size)

out = cv2.VideoWriter(output_video_name,fourcc,frame_per_second,size)

for i in range(count):
   img=cv2.imread("frame%d.jpg" %i)
   out.write(img)
    
out.release()
print(output_video_name) 
cv2.destroyAllWindows()   
        
       

    