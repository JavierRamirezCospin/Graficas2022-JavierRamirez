# Javier Ramirez Cospin, No. 18099
# Class used for utility functions

import struct

def char(var):
    return struct.pack('=c',var.encode('ascii'))

def word(var):
    return struct.pack('=h',var)

def dword(var):
    return struct.pack('=l',var)

# r, g, b must be normalized (0.0 - 1.0)
def Color(r,g,b):
    return bytes([int(255*b),
                  int(255*g),
                  int(255*r)])
