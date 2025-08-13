import qrcode

url = 'https://github.com/CiccioBro17'

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)

qr.add_data(url)

qr.make(fit=True)

img = qr.make_image(fill_color="#189BCC", back_color="black")

img.save("ciccio.jpeg")