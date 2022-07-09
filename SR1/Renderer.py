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
        self.paint_color = Color(1.0,1.0,1.0)

    # Function used to define image
    def glCreateWindow(self,width,height)->None:
        self.framebuffer = []
        self.width = width
        self.height = height

    # Function used to define viewport
    def glViewPort(self,x,y,width,height)->None:
        self.viewport_x = x
        self.viewport_y = y
        self.viewport_w = width
        self.viewport_h = height

    # Function to set pixel colors
    # r, g, b must be normalized (0.0 - 1.0)
    def glColor(self,r=1.0,g=1.0,b=1.0)->None: 
        self.paint_color = Color(r,g,b)

    # Function to draw pixel on image
    def glVertex(self,x,y)->None:
        self.framebuffer[y][x] = self.paint_color

    # Function to set image background color
    # r, g, b must be normalized (0.0 - 1.0)
    def glClearColor(self,r=0.0,g=0.0,b=0.0)->None: 
        self.clear_color = Color(r,g,b)

    # Function for Clearing image
    # r, g, b must be normalized (0.0 - 1.0)
    def glClear(self,r=0,g=0,b=0)->None:
        self.framebuffer = [[self.clear_color for x in range(self.width)]
                            for y in range(self.height)]

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
        
        finish = round(timer() - self.start,6)
        print("> Total time: " + str(finish) + " s")