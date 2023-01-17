import pyqrcode
from pyqrcode import QRCode

url = "https://github.com/wkndavid"
criar = pyqrcode.create(url)
criar.svg('myRepository.svg', scale=3)
criar.png('myRepository.png', scale=3)