# Javier Ramirez Cospin, No. 18099
# Class used for rendering final image

from Renderer import Renderer
import random

rend = Renderer(1024,1024)
rend.glClear()
# Polygon 1
rend.glDrawPolygon([(165, 380),(185, 360),(180, 330),(207, 345),(233, 330),
                    (230, 360),(250, 380),(220, 385),(205, 410),(193, 383)])
# Polygon 2
rend.glDrawPolygon([(321, 335),(288, 286),(339, 251),(374, 302)])
# Polygon 3
rend.glDrawPolygon([(377, 249),(411, 197),(436, 249)])
# Polygon 4
rend.glDrawPolygon([(413, 177),(448, 159),(502, 88),(553, 53),(535, 36),
                    (676, 37),(660, 52),(750, 145),(761, 179),(672, 192),
                    (659, 214),(615, 214),(632, 230),(580, 230),(597, 215),
                    (552, 214),(517, 144),(466, 180)])
# Polygon 5
rend.glDrawPolygon([(682, 175),(708, 120),(735, 148),(739, 170)])



rend.glFinish('output.bmp')