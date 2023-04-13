#This script convert all images from the folder to grsyscale

from PIL import Image
from os import listdir


def rgba2l(imgPath, savePath):
	
	imgsNames = listdir(imgPath)
	[Image.open(imgPath + name).convert("L").save(savePath + name) for name in imgsNames]

	print("Done!")


imgPath  = "imgPath/"
savePath = "savePath/"

rgba2l(imgPath, savePath)
