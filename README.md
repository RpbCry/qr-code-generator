# QR Code Generator
The QR Code Generator is a simple Python application that allows users to generate QR codes based on the input URL provided by the user. The generated QR code is displayed in a graphical user interface (GUI) using the tkinter library.

## Requirements
Before running the QR Code Generator, make sure you have the following dependencies installed:
`Python 3.x`
`qrcode library`
`Pillow library (PIL fork)`
You can install the required libraries using pip:
```
pip install qrcode[pil]
```

## How to Use
Clone or download this repository to your local machine.
Run the qr_code_generator.py script:
```
python qr_code_generator.py
```
A tkinter window will appear, prompting you to enter the URL for which you want to generate the QR code.
Enter the URL in the input field and click the `Generate QR Code` button.
The QR code corresponding to the entered URL will be generated and displayed in the GUI.
You can repeat the process to generate QR codes for different URLs.

## Note
The QR code image is temporarily saved as `temp_qr_code.png` in the local directory for display purposes. The temporary file is deleted automatically after displaying the QR code. If you want to retain the generated QR code, please manually save it before closing the application.

## License
This project is licensed under the MIT License.

Feel free to use, modify, and distribute the QR Code Generator as per the terms of the MIT License.

## Acknowledgments
The QR Code Generator is built using the following open-source libraries:

`qrcode`
`Pillow`
Thanks to the developers of these libraries for their contributions to the open-source community.
