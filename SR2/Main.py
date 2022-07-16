# Javier Ramirez Cospin, No. 18099
# Class used for rendering final image

from math import cos, sin
from Renderer import Renderer
import random

rend = Renderer(512,512)
rend.glClear()
# Temporal function to create random points on image
for k in range(8):
    prob = random.randrange(0,3)
    if prob == 0: rend.glColor(1.0,0.0,0.0)
    elif prob == 1: rend.glColor(0.0,1.0,0.0)
    elif prob == 2: rend.glColor(0.0,0.0,1.0)
    p1_x = random.randrange(0,512)
    p1_y = random.randrange(0,512)
    p2_x = random.randrange(0,512)
    p2_y = random.randrange(0,512)
    p3_x = random.randrange(0,512)
    p3_y = random.randrange(0,512)
    rend.glLine(p1_x,p1_y,p2_x,p2_y)
    rend.glLine(p2_x,p2_y,p3_x,p3_y)
    rend.glLine(p1_x,p1_y,p3_x,p3_y)

rend.glFinish('example2.bmp')
