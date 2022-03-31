from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

OUTPUT_PATH = 'output#3banner'

for i in range(1, 2):
	img = Image.open("resource/banner/bar3500.png")
	draw = ImageDraw.Draw(img)
	# font = ImageFont.truetype(<font-file>, <font-size>)
	font = ImageFont.truetype('resource/front/SOURCEHANSANSCN-REGULAR_0.OTF', 65)
	# draw.text((x, y),"Sample Text",(r,g,b))
	draw.text((1600, 120), str(i).zfill(4), (240, 209, 145), font=font)
	img.show()
	# img.save('{}/{}.png'.format(OUTPUT_PATH, i))


