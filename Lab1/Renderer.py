# Javier Ramirez Cospin, 18099 
# Class used for creating bmp images

from timeit import default_timer as timer
from Utils import char, word, dword, Color

# Class used for rendering images
class Renderer(object):
    # Class consructor
    def __init__(self,width,height)->None:
        self.glInit()
        self.glCreateWindow(width,height)

    # Function used for setting initial parameters
    def glInit(self)->None:
        self.start = timer()
        self.clear_color = Color(0.0,0.0,0.0)
        self.p_color = Color(1.0,1.0,1.0)

    # Function used to define image
    def glCreateWindow(self,width,height)->None:
        self.framebuffer = []
        self.width = width
        self.height = height

    # Function to set image background color
    # r, g, b must be normalized (0.0 - 1.0)
    def glClearColor(self,r=0.0,g=0.0,b=0.0)->None: 
        self.clear_color = Color(r,g,b)

    # Function used to define viewport
    def glViewPort(self,x,y,width,height)->None:
        self.vp_x = x
        self.vp_y = y
        self.vp_w = width
        self.vp_h = height

    # Function for clearing image WITHOUT viewport
    def glClear(self)->None:
        self.framebuffer = [[self.clear_color for x in range(self.width)]
                            for y in range(self.height)]

    # Function for clearing image WITH viewport
    # r, g, b must be normalized (0.0 - 1.0)
    def glClearVP(self,r=1.0,g=1.0,b=1.0)->None:
        for x in range(self.vp_x,self.vp_x+self.vp_w):
            for y in range(self.vp_y,self.vp_y+self.vp_h):
                self.glVertex(x,y)

    # Function to set pixel colors
    # r, g, b must be normalized (0.0 - 1.0)
    def glColor(self,r=1.0,g=1.0,b=1.0)->None: 
        self.p_color = Color(r,g,b)

    # Function to draw pixel WITHOUT viewport
    def glVertex(self,x,y)->None:
        if 0 > x or x > self.width-1: return
        if 0 > y or y > self.height-1: return
        self.framebuffer[y][x] = self.p_color

    # Function to draw pixel WITH viewport
    # x, y must be normalized (-1.0 - 1.0)
    def glVertexVP(self,posX,posY)->None:
        if (-1 > posX > 1) or (-1 > posY > 1): return
        x = int((posX+1)*(self.vp_w/2) + self.vp_x)
        y = int((posY+1)*(self.vp_h/2) + self.vp_y)
        self.glVertex(x,y)

    # Bresenham line Function to draw line from (x0,y0) to (x1,y1)
    def glLine(self,x0,y0,x1,y1):
        steep = abs(y1 - y0) > abs(x1 - x0)
        if steep:
            x0, y0 = y0, x0
            x1, y1 = y1, x1
        if x0 > x1: 
            x0, x1 = x1, x0
            y0, y1 = y1, y0
        offset = 0
        limit = 0.5
        m = abs(y1 - y0) / abs(x1 - x0)
        y = y0
        for x in range(x0,x1+1):
            if steep: self.glVertex(y,x)
            else: self.glVertex(x,y)
            offset += m
            if offset >= limit:
                if y0 < y1: y += 1
                else: y -= 1
                limit += 1

    # Function used to draw outlines of polygon
    def glDrawPolygon(self,vertices):
        for v in range(len(vertices)):
            start = vertices[v]
            final = vertices[(v+1) % len(vertices)]
            self.glLine(start[0],start[1],final[0],final[1])

    # Function to Show compilation time
    def ShowTime(self):
        finish = round(timer() - self.start,6)
        print("> Total time: " + str(finish) + " s")

    # Function for renderizing final
    def glFinish(self,filename)->None:
        with open(filename,'bw') as f:
            # Header
            f.write(char('B'))
            f.write(char('M'))
            f.write(dword(14 + 40 + self.width * self.height * 3))
            f.write(dword(0))
            f.write(dword(14 + 40))
            # Offset
            f.write(dword(40))
            f.write(dword(self.width))
            f.write(dword(self.height))
            f.write(word(1))
            f.write(word(24))
            f.write(dword(0))
            f.write(dword(self.width * self.height * 3))
            f.write(dword(0))
            f.write(dword(0))
            f.write(dword(0))
            f.write(dword(0))
            for x in range(self.height):
                for y in range(self.width):
                    f.write(self.framebuffer[x][y])
        # Show Compilation time
        self.ShowTime()
        