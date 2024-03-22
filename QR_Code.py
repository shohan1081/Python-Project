import pyqrcode 
from pyqrcode import QRCode
s = "https://www.facebook.com/shohanul.islam.1/"
url=pyqrcode.create(s)
url.svg("QR_Facebook.svg",scale=20)