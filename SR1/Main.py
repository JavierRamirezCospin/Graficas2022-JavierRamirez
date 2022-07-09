# Javier Ramirez Cospin, No. 18099
# Class used for rendering final image

from Renderer import Renderer
import random

rend = Renderer(1024,512)
rend.glClear()
# Temporal function to create random points on image
for x in range(1000):
    rend.glVertex(random.randrange(0,1024),random.randrange(0,512))
rend.glFinish('example.bmp')
