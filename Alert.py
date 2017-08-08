'''Doc String'''
import ctypes
import sys
STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE = -11
STD_ERROR_HANDLE = -12
FOREGROUND_BLACK = 0x00  # black.
FOREGROUND_DARKBLUE = 0x01  # dark blue.
FOREGROUND_DARKGREEN = 0x02  # dark green.
FOREGROUND_DARKSKYBLUE = 0x03  # dark skyblue.
FOREGROUND_DARKRED = 0x04  # dark red.
FOREGROUND_DARKPINK = 0x05  # dark pink.
FOREGROUND_DARKYELLOW = 0x06  # dark yellow.
FOREGROUND_DARKWHITE = 0x07  # dark white.
FOREGROUND_DARKGRAY = 0x08  # dark gray.
FOREGROUND_BLUE = 0x09  # blue.
FOREGROUND_GREEN = 0x0a  # green.
FOREGROUND_SKYBLUE = 0x0b  # skyblue.
FOREGROUND_RED = 0x0c  # red.
FOREGROUND_PINK = 0x0d  # pink.
FOREGROUND_YELLOW = 0x0e  # yellow.
FOREGROUND_WHITE = 0x0f  # white.

# Windows CMD命令行 背景颜色定义 background colors
BACKGROUND_BLUE = 0x10  # dark blue.
BACKGROUND_GREEN = 0x20  # dark green.
BACKGROUND_DARKSKYBLUE = 0x30  # dark skyblue.
BACKGROUND_DARKRED = 0x40  # dark red.
BACKGROUND_DARKPINK = 0x50  # dark pink.
BACKGROUND_DARKYELLOW = 0x60  # dark yellow.
BACKGROUND_DARKWHITE = 0x70  # dark white.
BACKGROUND_DARKGRAY = 0x80  # dark gray.
BACKGROUND_BLUE = 0x90  # blue.
BACKGROUND_GREEN = 0xa0  # green.
BACKGROUND_SKYBLUE = 0xb0  # skyblue.
BACKGROUND_RED = 0xc0  # red.
BACKGROUND_PINK = 0xd0  # pink.
BACKGROUND_YELLOW = 0xe0  # yellow.
BACKGROUND_WHITE = 0xf0  # white.
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)


class Alert():
    '''A Class used to print'''

    def __init__(self):
        self.counter = 0
        self.set_cmd_text_color(FOREGROUND_RED | FOREGROUND_GREEN |
                                FOREGROUND_BLUE)
        if __name__ == "__main__":
            print("class {} initialized".format(self.__class__.__name__))

    def set_cmd_text_color(self, color, handle=std_out_handle):
        Bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
        return Bool

    def resetColor(self):
        self.set_cmd_text_color(FOREGROUND_RED | FOREGROUND_GREEN |
                                FOREGROUND_BLUE)

    def Warn(self, string, color=FOREGROUND_YELLOW, end_of_text='\n'):
        self.counter += 1
        self.set_cmd_text_color(color)
        # .format(self.stdlz(), string)
        # sys.stdout.write("Warning %s : %s\n" % (self.stdlz(), string))
        print("Warning %s : %s" % (self.stdlz(), string), end=end_of_text)
        self.resetColor()
        # print("Warning {} : {}".format(self.stdlz(), string))

    def Info(self, string, color=FOREGROUND_GREEN, end_of_text='\n'):
        self.counter += 1
        self.set_cmd_text_color(color)
        print("Info    %s : %s" % (self.stdlz(), string), end=end_of_text)
        self.resetColor()

    def colorPrint(self, string, color=FOREGROUND_WHITE, end_of_text=' '):
        self.set_cmd_text_color(color)
        print("%s" % string, end=end_of_text)
        self.resetColor()

    def stdlz(self):
        if self.counter > 999999:
            self.counter = 1
        restr = str(self.counter)
        length = len(restr)
        while length < 6:
            restr = '0' + restr
            length = len(restr)
        return (restr)
