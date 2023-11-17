from pwn import xor
import cv2
from pyzbar.pyzbar import decode
img = bytes.fromhex("F9 3E 29 21 62 78 7F 64")
actual = bytes.fromhex("89 50 4E 47 0D 0A 1A 0A")

print(xor (img,actual).decode('UTF-8'))

def xor_image_with_key(image_path, key):
    
    with open(image_path, 'rb') as file:
        image_data = bytearray(file.read())

    key_bytes = key.encode('utf-8')
    key_length = len(key_bytes)

    for i in range(len(image_data)):
        image_data[i] ^= key_bytes[i % key_length]

    output_path = f"xored_{image_path}"
    with open(output_path, 'wb') as output_file:
        output_file.write(image_data)
    
    print(f"XOR operation with key '{key}' completed. Result saved to {output_path}")
    return output_path

def read_qr_code(xored_image_path):
    
    image = cv2.imread(xored_image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    qr_codes = decode(gray_image)

    if not qr_codes:
        print("No QR code found in the image.")
        return

    for qr_code in qr_codes:
        qr_data = qr_code.data.decode('utf-8')
        print(f"The Flag is: {qr_data}")

if __name__ == "__main__":
    img = bytes.fromhex("F9 3E 29 21 62 78 7F 64")
    actual = bytes.fromhex("89 50 4E 47 0D 0A 1A 0A")

    print("The key is:", xor(img,actual).decode('UTF-8'))
    image_path = "encrypted.png"
    key = xor(img,actual).decode('UTF-8')
    output_path = xor_image_with_key(image_path, key)
    xored_image_path = output_path 
    read_qr_code(xored_image_path)
