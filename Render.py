import os
import termcolor as tc
import ctypes
kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

class ASCIIRender(object):

    ColorBufffer = []
    ZBuffer = []

    def size(self, ):
        get_size = os.get_terminal_size()
        size = list(get_size)
        
        return size

    def font(self, color, on_color, size_in):
        size = size_in
        font = [' ' for i in range(size[0] * (size[-1]))]
        for i in font:
            tc.cprint(i, color, on_color, end='', sep='')

    def Render(ColorBuffer, sizeinfunction):
        ColorBuffer
        size = sizeinfunction
        #for i in range(size[0] * (size[1]-1)):
        #    ColorBuffer[]


ASCII_Instance = ASCIIRender()
size = ASCII_Instance.size()
ASCII_Instance.font('white', 'on_white', size)
