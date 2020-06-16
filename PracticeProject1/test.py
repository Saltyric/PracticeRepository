from PyQt5.QtGui import *
import os

img = QImage()
path = "./img"
for root, dirs, files in os.walk(path):
    for name in files:
        print(name)
        if name.endswith(".png"):
            print(name)
            print("./img/" + name)
            img.load("./img/" + name)
            img.save("./img/" + name)