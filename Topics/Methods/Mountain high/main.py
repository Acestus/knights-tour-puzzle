class Mountain:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    # create convert_height here
    def convert_height(self):
        self.height_feet = self.height / 0.3048
        return self.height_feet