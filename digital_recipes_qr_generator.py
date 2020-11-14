from qrcode import QRCode

from recipe_links import RECIPE_LINKS


DIGITAL_RECIPE_QR_CODES_FILE_PATH='digital_recipes_qr_code'

qr = QRCode(
    version=1, # controls the size of the QR code: 1-40, 1 being the smallest (21x21 matrix)
    box_size=10, # controls the number of pixels for each QR code "box"
    border=4, # controls the thickness of the box border
)
for name, link in RECIPE_LINKS.items():
    qr.add_data(link) # accepts hyperlink
    qr.make() # ensures that the entire dimension of the QR code is utilize
    img = qr.make_image(fill_color='#0f346c', back_color='white')
    img.save(f'{DIGITAL_RECIPE_QR_CODES_FILE_PATH}/{name}_qr_code.png')
    qr.clear()
