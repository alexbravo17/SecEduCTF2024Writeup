### Encoded, secret message?

Given Ciphertext
> 籜籎籌籎籍籞粄籮籷籬簹籭籲籷籰籨籶簽籼籽簼类籨簹类籨籼簹籶簼籽籱簺籷籰粆

This is probably Unicode/UTF-8 file since it is chinese characters

hex:
e7b19ce7b18ee7b18ce7b18ee7b18de7b19ee7b284e7b1aee7b1b7e7b1ac
e7b0b9e7b1ade7b1b2e7b1b7e7b1b0e7b1a8e7b1b6e7b0bde7b1bce7b1bd
e7b0bce7b1bbe7b1a8e7b0b9e7b1bbe7b1a8e7b1bce7b0b9e7b1b6e7b0bc
e7b1bde7b1b1e7b0bae7b1b7e7b1b0e7b2860a

Base64:
57Gc57GO57GM57GO57GN57Ge57KE57Gu57G357Gs57C557Gt57Gy57G357Gw57Go57G257C957G8
57G957C857G757Go57C557G757Go57G857C557G257C857G957Gx57C657G357Gw57KGCg==

This seems like a deadend, not sure so lets look at hint.

Hint: ROT seems like a common cipher used

Using cyberchef, ROT-8000 got flag **SECEDU{enc0ding_m4st3r_0r_s0m3th1ng}**