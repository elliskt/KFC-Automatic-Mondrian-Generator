import cv2
import utils
from PIL import Image
import numpy as np
import colorsys
import random
import shutil
import os
count = 1
for i in os.listdir('C:\\Users\IcarusArt.AI\Desktop\kfc_0001-3500'):
	print(i)
	for j in os.listdir('{}/{}'.format('C:\\Users\IcarusArt.AI\Desktop\kfc_0001-3500', i)):
		print(j)
		shutil.copy('{}/{}/{}'.format('C:\\Users\IcarusArt.AI\Desktop\kfc_0001-3500', i, j), 'standard-3500/{}.png'.format(count))
		count += 1
