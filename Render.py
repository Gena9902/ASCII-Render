import win32console
import os
import termcolor as tc
import ctypes
kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)


os.system(f'mode con: cols={100} lines={40}')
class ASCIIRender(object):

    ColorBuffer = []
    ZBuffer = []

    def __init__(self):
        self.screenBuffer = win32console.GetStdHandle(win32console.STD_OUTPUT_HANDLE)
        self.consoleResolution = (100, 40)

    def background(self, color):
        Pixel = tc.colored(' ', color, 'on_'+color)
        for i in range(self.consoleResolution[0] * self.consoleResolution[1]):
            self.screenBuffer.WriteConsole(Pixel)
        #self.screenBuffer.FillConsoleOutputCharacter(
        #    Pixel, self.consoleResolution[0]*self.consoleResolution[1], win32console.PyCOORDType(0, 0))
        

    def Circle(self, R, x1, y1, color, ColorBuffer):
        disp_x = x1
        disp_y = y1
        x = 0
        y = R
        delta = 1 - 2 * R
        error = 0
        Pixel = tc.colored(' ', color, 'on_'+color)
        while y >= x:
            ColorBuffer[disp_x + x1][disp_y + y] = Pixel
            ColorBuffer[disp_x + x1][disp_y + y] = Pixel
            ColorBuffer[disp_x + x1][disp_y + y] = Pixel
            ColorBuffer[disp_x + x1][disp_y + y] = Pixel

            error = 2 * (delta + y) -1
            if delta < 0 and error <= 0:
                x += 1
                delta = delta + (2 * x + 1)
                continue
            if delta > 0 and error > 0:
                y -= 1
                delta = delta + (1 - 2 * y)
                continue    
            x += 1
            delta = delta + (2 * (x - y))
            y -= 1
        
        return ColorBuffer

    def render(self):
        for i in self.ColorBuffer:
            print(i, end='', sep='')


#os.system('cls')
ASCII_Instance = ASCIIRender()
print((tc.colored(' ', 'green', 'on_green')))
#R = int(input('Введите радиус круга(целое не нулевое число): '))
#x0 = int(size[0]/2)
#y0 = int(size[1]/2)
ASCII_Instance.background('white')
#ASCII_Instance.render()

'''
if (R > size[0]/2) or (R > size[1]/2) or (type(R) != int):
    print('Радиус превышает размер терминала или задан не корректно')
    if R < 0:
        R = abs(R)
        print('Защита от дурака. Ты че? Радиус не может быть отрицательным')
else:
    Circle = ASCII_Instance.Circle(R, x0, y0, 'red', ColorBuffer)
    ASCII_Instance.Render(size, Circle)
'''