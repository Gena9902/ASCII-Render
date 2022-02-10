import os
import termcolor as tc

class ASCIIRender(object):

    ColorBufffer = []
    ZBuffer = []

    def size(self, ):
        get_size = os.get_terminal_size()
        size = list(get_size)
        
        return size

    def font(self, color, size_in):
        size = size_in
        font = [' ' for i in range(size[0] * (size[1]-1))]
        for i in font:
            tc.cprint(i, 'color', end='', sep='')

    def Render(ColorBuffer, sizeinfunction):
        ColorBuffer
        size = sizeinfunction
        #for i in range(size[0] * (size[1]-1)):
        #    ColorBuffer[]
