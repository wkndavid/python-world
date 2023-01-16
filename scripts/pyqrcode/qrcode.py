import pyqrcode

url = pyqrcode.create("https://github.com/wkndavid/python-world/tree/main/scripts/pyqrcode")
url.png("pyqrcode_repository", scale=5)
url.svg("pyqrcode_repository", scale=6)
