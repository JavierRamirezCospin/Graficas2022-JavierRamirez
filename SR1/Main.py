# Javier Ramirez Cospin, No. 18099
# Class used for rendering final image

from Renderer import Renderer
import random

rend = Renderer(512,512)
rend.glClear()
# Temporal function to create random points on image
#for x in range(2000):
    # rend.glColor(1.0,1.0,random.uniform(0.6,1.0))
    # rend.glVertex(random.randrange(0,512),random.randrange(0,512))
rend.glViewPort(0,0,256,256)
rend.glClearVP()
rend.glColor(0.0,0.0,0.0)
rend.glVertexVP(0,0)
rend.glFinish('example.bmp')
