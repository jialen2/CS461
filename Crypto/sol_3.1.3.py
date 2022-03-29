import sys
from Crypto.Cipher import AES

if len(sys.argv) != 5:
    print("invalid input")
    exit(1)
ciphertext_file, key_file, iv_file, output_file = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
with open(ciphertext_file) as f:
    file_content = f.read().strip()
    ciphertext_binary = bytes.fromhex(file_content)
with open(key_file) as f:
    file_content = f.read().strip()
    key_binary = bytes.fromhex(file_content)
with open(iv_file) as f:
    file_content = f.read().strip()
    iv_binary = bytes.fromhex(file_content)
cipher = AES.new(key_binary, AES.MODE_CBC, iv=iv_binary)
plaintext = cipher.decrypt(ciphertext_binary)
with open(output_file, "w") as output:
    output.write(plaintext.decode("utf-8"))
