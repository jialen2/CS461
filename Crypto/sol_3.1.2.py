import sys

if len(sys.argv) != 4:
    print("invalid input")
    exit(1)
ciphertext_file, key_file, output_file = sys.argv[1], sys.argv[2], sys.argv[3]
ascii_to_key = {}
with open(key_file, "r") as input:
    line = input.readline()
    for i in range(26):
        ascii_to_key[line[i]] = chr(ord('A') + i)
decrypted_str = ""
with open(ciphertext_file, "r") as input:
    line = input.readline()
    for ch in line:
        if ch.isalpha():
            decrypted_str += ascii_to_key[ch]
        else:
            decrypted_str += ch
with open(output_file, "w") as output:
    output.write(decrypted_str)
