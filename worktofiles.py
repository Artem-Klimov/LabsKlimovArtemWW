import time

class MyContextManager:
    def __init__(self, file):
        self.file = file
        self.level = 0
        self.e = None

    def __enter__(self):
        if self.level == 0:
            self.e = None

        self.level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1


    def __float__(self):
        pass

    def write(self, text):
        self.file.write("    " * self.level + text + "\n")


with open("result.txt", "w") as file:
    mcm = MyContextManager(file)

    mcm.write("None indent :(")

    with mcm:
        mcm.write("MAIIII <3 <3 <3")

        with mcm:
            mcm.write("Two indent *_*")

        mcm.write("One indent :O")

    mcm.write("None indent :/")
