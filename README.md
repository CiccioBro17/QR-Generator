# QR Generator

This project is a simple Python script to generate a QR code for a specified URL. The generated QR code is saved as an image file (`str_qr.jpeg`).

## Features
- Generates a QR code for a given URL
- Customizable QR code color and background
- Saves the QR code as a JPEG image

## Requirements
- Python 3.x
- `qrcode` library

## Installation
1. Clone this repository or download the script.
2. Install the required Python package:
   ```bash
   pip install qrcode[pil]
   ```

## Usage
Run the script using Python:
```bash
python3 main.py
```
This will generate a QR code image (`str_qr.jpeg`) in the project directory for the URL specified in the script.

## Customization
- To change the URL, edit the `url` variable in `main.py`.
- You can also modify the QR code's color and background by changing the `fill_color` and `back_color` parameters in the script.

## License
This project is licensed under the MIT License.
