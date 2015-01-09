class Environment:

    def __init__(self):
        import numpy
        self.width = 10
        self.length = 10
        self.resolution = .5
        self.xx = numpy.arange(-self.length, self.length, self.resolution)
    # def visualize(self):
