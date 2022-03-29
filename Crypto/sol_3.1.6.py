import sys

def WHA(input_str):
    input_str = input_str.encode("utf-8")
    mask = int("3FFFFFFF", 16)
    out_hash = 0
    for byte in input_str:
        a = (byte ^ int("CC", 16)) << 24
        b = (byte ^ int("33", 16)) << 16
        c = (byte ^ int("AA", 16)) << 8
        d = (byte ^ int("55", 16))
        intermediate = a | b | c | d 
        out_hash = (out_hash & mask) + (intermediate & mask)
    return hex(out_hash)

if len(sys.argv) != 3:
    print("invalid input")
    exit(1)
input_file, output_file = sys.argv[1], sys.argv[2]
with open(input_file) as f:
    input_str = f.read().strip()
hashed_str = WHA(input_str)
with open(output_file, "w") as f:
    f.write(hashed_str)