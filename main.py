import qrcode

url = 'https://play.google.com/store/apps/details?id=com.simracing.toolbox'

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)

qr.add_data(url)

qr.make(fit=True)

img = qr.make_image(fill_color="#006f00", back_color="black")

img.save("str_qr.jpeg")