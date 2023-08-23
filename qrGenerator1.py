# Import the necessary libraries
import qrcode
from PIL import Image

# Create a QR code object with specified settings
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)

# Add the data (URL) to the QR code
qr.add_data("https://www.linkedin.com/in/shriya-srivastava-90555421")

# Generate the QR code pattern
qr.make(fit=True)

# Create an image from the QR code object with customized colors
img = qr.make_image(fill_color="#FFA500", back_color="#006400")

# Save the generated image to a file
img.save("ShriyaSri_linkdln.png")

