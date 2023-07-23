import tkinter as tk
import qrcode
from PIL import Image, ImageTk

def generate_qr_code():
    url = url_entry.get()

    # Generate the QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code image as a temporary file
    temp_qr_file = "temp_qr_code.png"
    img.save(temp_qr_file)

    # Display the QR code in the GUI
    qr_img = Image.open(temp_qr_file)
    qr_img = qr_img.resize((200, 200))

    qr_photo = ImageTk.PhotoImage(qr_img)
    qr_label.config(image=qr_photo)
    qr_label.image = qr_photo

    # Optional: Delete the temporary QR code file after displaying
    # This step is optional and can be omitted if you don't want to delete the file
    import os
    if os.path.exists(temp_qr_file):
        os.remove(temp_qr_file)

# Create the main tkinter window
root = tk.Tk()
root.title("QR Code Generator")

# URL input
url_entry = tk.Entry(root, width=30)
url_entry.pack(pady=10)

# Button to generate QR code
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr_code)
generate_button.pack(pady=5)

# Label to display QR code
qr_label = tk.Label(root)
qr_label.pack(pady=10)

root.mainloop()
