# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 10:40:20 2020

@author: parneet
"""

import cv2
from PIL import Image
import sys
import mimetypes
inp = str(sys.argv[1])
try:
    X = int(sys.argv[2])
except:
    print('Error!! Compress index is not passed')
    exit()
if len(sys.argv)>3:
    print('Error !! More parameters passed')
    exit()
else:
    pass
if X>0 and X<100:
    pass
else:
    print('Error!! Compression size invalid')
    exit()
mimestart = mimetypes.guess_type(inp)
try:
    mimestart == 'video'
except:
    print("\nUnsupported Format\n")
try:
    p = open(inp)
except:
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
        height,width,layers = image.shape
        size1 = (width)
        size2 = (height)
        p1 = ((100 - X) / 100) * size1
        p2 = ((100 - X) / 100) * size2
        
        cv2.imwrite("frame%d.jpg" % count, image)
        image = Image.open('frame%d.jpg' %count)
        
        image.thumbnail((p2, p1))
        
        image.save('frame%d.jpg' %count)
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