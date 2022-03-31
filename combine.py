import os
from PIL import Image
import utils
from PIL import ImageFont
from PIL import ImageDraw

banner_path = 'output#3banner'
gen_path = 'standard-3500'
kfc_100 = os.listdir('C:\\Users\IcarusArt.AI\Desktop\KFC\\standard-3500')
output_path = 'output#Standard-3500'
utils.mkdir(output_path)
# ---


count = 1
for i in kfc_100:
	# --- load image
	img = Image.open('{}/{}'.format(gen_path, i))
	# ---
	banner = Image.open("resource/banner/bar3500.png")
	draw = ImageDraw.Draw(banner)
	# font = ImageFont.truetype(<font-file>, <font-size>)
	font = ImageFont.truetype('resource/front/SOURCEHANSANSCN-REGULAR_0.OTF', 65)
	# draw.text((x, y),"Sample Text",(r,g,b))
	draw.text((1600, 120), str(count).zfill(4), (240, 209, 145), font=font)
	# ---
	logo = Image.open('resource/logo/kfc.png')
	# --- paste logo
	# banner.paste(logo, (0, 0), logo)
	# --- new canvas
	bg_new = Image.new('RGBA', (img.width, img.height + banner.height))
	bg_new.paste(img, (0, 0))
	bg_new.paste(logo, (0, 0), logo)
	bg_new.paste(banner, (0, img.height))
	bg_new.save('{}/{}.png'.format(output_path, count), 'PNG')
	print(count)
	count += 1

