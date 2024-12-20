import qrcode # type: ignore

# Data to encode, attach link
data = "https://www.youtube.com/"

# Create QR Code object
qr = qrcode.QRCode(
    version=2,  # Controls the size of the QR Code (1 = smallest, 40 = largest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=20,  # Size of each box in pixels
    border=8,  # Border size in boxes
)

# Add data to the QR Code
qr.add_data(data)
qr.make(fit=True)

# Generate and save the QR Code image
img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode_example.png")