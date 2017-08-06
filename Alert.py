class Alert():
    def __init__(self):
        self.counter = 0
        print("##################################################")
        if __name__ == "__main__":
            print("class {} initialized".format(self.__class__.__name__))

    def Warn(self, string):
        self.counter += 1
        print("Warning {} : {}".format(self.stdlz(), string))

    def Info(self, string):
        self.counter += 1
        print("Info {} : {}".format(self.stdlz(), string))

    def stdlz(self):
        if self.counter > 999999:
            self.counter = 1
        restr = str(self.counter)
        length = len(restr)
        while length < 6:
            restr = '0' + restr
            length = len(restr)
        return (restr)
