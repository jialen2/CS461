import sys

if len(sys.argv) != 5:
    print("invalid input")
    exit(1)
ciphertext_file, key_file, modulo_file, output_file = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
with open(ciphertext_file) as f:
    file_content = f.read().strip()
    ciphertext_binary = int(file_content,16)
with open(key_file) as f:
    file_content = f.read().strip()
    key_binary = int(file_content,16)
with open(modulo_file) as f:
    file_content = f.read().strip()
    modulo_binary = int(file_content,16)
plaintext = hex((ciphertext_binary ** key_binary) % modulo_binary)[2:]
with open(output_file, "w") as output:
    output.write(plaintext)
