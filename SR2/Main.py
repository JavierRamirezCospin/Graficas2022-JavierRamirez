# Javier Ramirez Cospin, No. 18099
# Class used for rendering final image

from math import cos, sin
from Renderer import Renderer
import random

rend = Renderer(512,512)
rend.glClear()
# Temporal function to create random points on image
for k in range(200):
    rend.glVertex(random.randrange(512),random.randrange(512))

for k in range(100):
    r0 = random.randrange(10,60)
    r1 = random.randrange(int(r0*2.0),int(r0*20))
    angle = random.randrange(0,361)
    x0 = int(r0*sin(angle))+256
    y0 = int(r0*cos(angle))+256
    x1 = int(r1*sin(angle))+256
    y1 = int(r1*cos(angle))+256
    rend.glColor(0.0,0.0,1.0)
    rend.glLine(x0,y0,x1,y1)

for k in range(150):
    r0 = random.randrange(13,60)
    r1 = random.randrange(int(r0*2.0),int(r0*20))
    angle = random.randrange(0,361)
    x0 = int(r0*sin(angle))+256
    y0 = int(r0*cos(angle))+256
    x1 = int(r1*sin(angle))+256
    y1 = int(r1*cos(angle))+256
    rend.glColor(0.0,0.67,1.0)
    rend.glLine(x0,y0,x1,y1)

for k in range(150):
    r0 = random.randrange(13,60)
    r1 = random.randrange(int(r0*2.0),int(r0*20))
    angle = random.randrange(0,361)
    x0 = int(r0*sin(angle))+256
    y0 = int(r0*cos(angle))+256
    x1 = int(r1*sin(angle))+256
    y1 = int(r1*cos(angle))+256
    rend.glColor(1.0,1.0,1.0)
    rend.glLine(x0,y0,x1,y1)

rend.glFinish('example.bmp')
