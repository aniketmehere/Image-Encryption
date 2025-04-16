from PIL import Image
import numpy as np
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

# Load an image
def load_image(image_path):
    img = Image.open(image_path)
    return img

# Convert image to bytes
def image_to_bytes(img):
    img = img.convert("RGB")
    img_array = np.array(img)
    return img_array.tobytes(), img.size, img_array.shape

# Convert bytes back to image
def bytes_to_image(byte_data, img_shape):
    img_array = np.frombuffer(byte_data, dtype=np.uint8)
    img_array = img_array.reshape(img_shape)
    return Image.fromarray(img_array)

# Generate a random AES key
def generate_key():
    return os.urandom(16)  # 128-bit key

# Encrypt image bytes using AES
def encrypt_data(data, key):
    cipher = AES.new(key, AES.MODE_CBC)
    padded_data = pad(data, AES.block_size)
    encrypted = cipher.iv + cipher.encrypt(padded_data)
    return encrypted

# Decrypt image bytes using AES
def decrypt_data(encrypted_data, key):
    iv = encrypted_data[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(encrypted_data[16:]), AES.block_size)
    return decrypted

# Save encrypted file
def encrypt_image_file(input_path, encrypted_path, key):
    img = load_image(input_path)
    image_bytes, _, _ = image_to_bytes(img)
    encrypted_bytes = encrypt_data(image_bytes, key)
    with open(encrypted_path, "wb") as f:
        f.write(encrypted_bytes)
    print("Image Encrypted Successfully!")

# Load encrypted file and decrypt
def decrypt_image_file(encrypted_path, output_path, key, original_shape):
    with open(encrypted_path, "rb") as f:
        encrypted_data = f.read()

    decrypted_bytes = decrypt_data(encrypted_data, key)
    decrypted_img = bytes_to_image(decrypted_bytes, original_shape)
    decrypted_img.save(output_path)
    print("Image Decrypted Successfully!")

# MAIN FUNCTION
if __name__ == "__main__":
    key = generate_key()

    # Paths
    input_img_path = "input_image.jpg"
    encrypted_img_path = "encrypted_image.bin"
    decrypted_img_path = "decrypted_image.jpg"

    # Step 1: Get image shape
    img = load_image(input_img_path)
    image_bytes, size, shape = image_to_bytes(img)

    # Step 2: Encrypt
    encrypt_image_file(input_img_path, encrypted_img_path, key)

    # Step 3: Decrypt
    decrypt_image_file(encrypted_img_path, decrypted_img_path, key, shape)
