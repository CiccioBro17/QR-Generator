import qrcode

url = 'https://linktr.ee/minghef1'

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)

qr.add_data(url)

qr.make(fit=True)

img = qr.make_image(fill_color="#FF2800", back_color="black")

img.save("minghe.jpeg")