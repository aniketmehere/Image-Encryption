# 🔐 Image Encryption System in Python

This project is a simple yet powerful tool to encrypt and decrypt images using **AES (Advanced Encryption Standard)** encryption in Python. It ensures that sensitive image data remains secure during transmission or storage.

## 📌 Features

- Encrypt any image using AES-128 (CBC Mode)
- Secure decryption with the same key
- Handles image-to-bytes conversion and back
- Uses industry-standard cryptography libraries
- Easy-to-understand and beginner-friendly

## 📁 Project Structure

```
ImageEncryptionProject/
│
├── main.py               # Main Python script
├── input_image.jpg       # Your original input image
├── encrypted_image.bin   # Encrypted binary file
├── decrypted_image.jpg   # Decrypted output image
└── README.md             # This documentation file
```

## ⚙️ Requirements

Make sure Python 3.x is installed.

Then install the required libraries:

```bash
pip install pillow numpy pycryptodome
```

## 🚀 How to Run

1. **Add your image**  
   Place your image file (e.g., `input_image.jpg`) in the project directory.

2. **Run the script**

```bash
python main.py
```

This will:
- Encrypt the `input_image.jpg` and save it as `encrypted_image.bin`
- Decrypt `encrypted_image.bin` and save the result as `decrypted_image.jpg`

## 🔐 How It Works

1. **Image Loading:** Pillow loads the image, NumPy converts it to a byte array.
2. **Encryption:** AES encrypts the image bytes using CBC mode with padding.
3. **Saving:** The encrypted data is saved as a `.bin` file.
4. **Decryption:** The script reads the encrypted file, decrypts it, and reconstructs the image.

## 🧪 Sample Output

- ✅ `input_image.jpg` (original)
- 🔒 `encrypted_image.bin` (binary data)
- 🔓 `decrypted_image.jpg` (restored image)

## 🛡️ Security Note

- This example uses a randomly generated AES key every time you run the script.
- For practical use, store and manage keys securely (e.g., using a secure key vault or password manager).  

## 📜 License

This project is licensed under the MIT License.
