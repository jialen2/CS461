from Crypto.Cipher import AES

with open("3.1.4_aes_weak_ciphertext.hex", "r") as input:
    file_content = input.read().strip()
    ciphertext_binary = bytes.fromhex(file_content)
        
for i in range(2 ** 5):
    hex_str = hex(i)[2:]
    key = 62 * '0' + (2 - len(hex_str)) * '0' + hex_str
    cipher = AES.new(bytes.fromhex(key), AES.MODE_CBC, iv=bytes.fromhex('0' * 32))
    plaintext = cipher.decrypt(ciphertext_binary)
    try:
        print(i, plaintext.decode("utf-8"))
        print(key)
    except:
        print("failed at :", i)
