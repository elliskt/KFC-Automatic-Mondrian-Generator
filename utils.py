from PIL import Image
import cv2
import os


def imshow_from_cv2(img):
	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	pil_im = Image.fromarray(img)
	pil_im.show()


def mkdir(path):
    try:
        os.mkdir(path)
        print("[INFO] SAVE IMAGE directory %s created" % path)
        return True
    except FileExistsError:
        print("[ERROR] SAVE IMAGE %s directory existed" % path)
        return False

