### Linkage

Got `jvvr8--ga0/76/5;/7:/317,cr/qmwvjgcqv/0,amorwvg,cocxmlcuq,amo-`
With signed key Y

First thought is ROT-13 and ROT-47, so let's try cyberchef again and try to brute-force or use Y = 24, 44
Nothing there, brute-forcing also does nothing

I have no more ideas, so try hint, which is a bad pun on XOR, so let's try XOR brute-force
Key = 2 gives http://ec2-54-79-58-135.ap-southeast-2.compute.amazonaws.com/

So the flag is **SECEDU{http://ec2-54-79-58-135.ap-southeast-2.compute.amazonaws.com/}**
