class Monitor:
    def __init__(self, model="", width=0, height=0):
        self.model = model
        self.width = width
        self.height = height

    def __add__(self, width, height):
        """Add monitor width to height"""
        return self.width + self.height
    def get_total_pixels(self):
        return self.width * self.height

    def get_resolution(self):
        """Return Monitor Resolution"""
        return (self.width, self.height)


Monitor1 = Monitor("Dell", 24, 10)
resolution = Monitor1.get_resolution()
print(Monitor1.width + Monitor1.height)
print(resolution)
