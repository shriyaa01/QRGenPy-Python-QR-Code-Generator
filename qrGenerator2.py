# Import the qrcode library as 'qr'
import qrcode as qr

# Generate a QR code with the provided URL
img = qr.make("https://github.com/shriyaa01/QRGenPy-Python-QR-Code-Generator")

# Save the generated image to a file
img.save("Code.png")

