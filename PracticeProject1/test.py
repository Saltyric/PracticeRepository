from PyQt5.QtGui import *
import os

img = QImage()
path = "./images"
for root, dirs, files in os.walk(path):
    for name in files:
        print(name)
        if name.endswith(".png"):
            print(name)
            print("./images/" + name)
            img.load("./images/" + name)
            img.save("./images/" + name)