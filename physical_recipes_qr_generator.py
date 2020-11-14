from qrcode import QRCode
from PIL import Image

from tips_and_tricks_links import TIPS_AND_TRICKS_LINKS

PHYSICAL_RECIPE_QR_CODES_FILE_PATH='physical_recipes_qr_code'
EXAMPLE_FILE='cheesy_chipotle_beef'
img_bg = Image.open(f'{PHYSICAL_RECIPE_QR_CODES_FILE_PATH}/{EXAMPLE_FILE}.jpg')

qr = QRCode(box_size=2)
qr.add_data(TIPS_AND_TRICKS_LINKS['how_to_chop_scallion_link'])
qr.make(fit=True)

img = qr.make_image()
pos = (img_bg.size[0] - img.size[0], img_bg.size[1] - img.size[1]) # right-bottom corner

img_bg.paste(img, pos)
img_bg.save(f'{PHYSICAL_RECIPE_QR_CODES_FILE_PATH}/{EXAMPLE_FILE}_qr_code.jpg')
