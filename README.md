# Vigenère Cipher Implementation

This repository contains a simple implementation of the **Vigenère Cipher**, a classical encryption algorithm used for encoding and decoding messages.

## Features
- Encrypts plaintext using a given keyword.
- Decrypts ciphertext back to plaintext using the same keyword.
- Interactive CLI interface.

## How It Works
The Vigenère Cipher is a method of encrypting alphabetic text by using a series of Caesar ciphers based on letters of a keyword. Each letter in the plaintext is shifted based on the corresponding letter in the repeating keyword.

## Usage
### Prerequisites
Ensure you have Python installed on your system.

### Running the Script
1. Clone this repository:
   ```bash
   git clone https://github.com/ItzAjall/vigenere-cipher.git
   ```
2. Navigate to the project directory:
   ```bash
   cd vigenere-cipher
   ```
3. Run the script:
   ```bash
   python vigenere-cipher.py
   ```
4. Follow the on-screen instructions:
   - Enter `E` to encrypt a message.
   - Enter `D` to decrypt a message.
   - Enter `X` to exit the program.

## Example
### Encryption
```
Encrypt/Decrypt/Exit (E/D/X): E
Plain Text: HELLO
Key: KEY
Cipher Text: RIJVS
```

### Decryption
```
Encrypt/Decrypt/Exit (E/D/X): D
Cipher Text: RIJVS
Key: KEY
Original Text: HELLO
```

## Issues & Contributions
Feel free to report any issues or contribute to improving the script by submitting a pull request.
