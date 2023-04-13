# Crop every single image of the folder to many with the size 256x256px and 100px overlap 

from PIL import Image
from os import listdir


def cropImgs(imgPath, savePath):
	
	names = listdir(imgPath)
	for name in names:
		img = Image.open(imgPath + name)
		width, height = img.size
		for w in range(0, width-256, 150):
			for h in range(0, height-256, 150):
				crpImg = img.crop((w, h, w+256, h+256))
				crpImg.save(savePath + name[:-4] + "_" + str(w) + "_" + str(h) + ".png")



imgPath   = "imgPath/"
savePath  = "savePath/"

cropImgs(imgPath, savePath)
