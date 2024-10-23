# QR is short for Quick Response, and they are named so because they can be read quickly by a cell phone. They are used to take information from transitory media and put it on your cell phone.

# QR codes are used to encode and decode the data into a machine-readable form. The use of camera phones to read two-dimensional barcodes for various purposes is currently a popular topic in both types of research and practical applications. 

# It contains a grid of black squares on a white background, which can be read by any imaging device such as a camera, and processed to extract the required data from the patterns that are present in the horizontal components of the image.

# To generate QR Codes with Python you need to install only one Python library for this task: " pyqrcode".


# Code : (this will give a vector of an svg and you can open it in the browser)
# import pyqrcode 
# from pyqrcode import QRCode 
# source = "https://www.google.com/"
# url = pyqrcode.create(source)
# url.svg("8-qr-code-image.svg", scale = 8)


# Code : (this will give you a png image)
import pyqrcode
from PIL import Image
source = "https://www.google.com/"
url = pyqrcode.create(source)
# Save as PNG
url.png("8-qr-code-image.png", scale=8)
img = Image.open("8-qr-code-image.png")
img.show()