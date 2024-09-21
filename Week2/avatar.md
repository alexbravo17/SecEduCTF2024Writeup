### Avatar

We have a website http://ec2-54-79-58-135.ap-southeast-2.compute.amazonaws.com/

There is a gravatar link, which when I looked up online, it can be brute-forced since it uses a SHA-256 hash of email address

https://2.gravatar.com/avatar/127a564647a8981b658a36e3cc9da08ec5d3f8437c3e4e336e2f43dcb862d7f0

Then theres the email address given `*************@*****.***`, so the email is 13 letters long, mail service is possibly gmail or yahoo (5 letters) then .com

`john --mask=?1?1?1?1?1?1?1?1?1?1?1?1?1@gmail.com --1=[a-z0-9] hash.txt --format=Raw-SHA256`

skateboarding
?1?1?1?1?1?1?1?1?1?1?1?1?1
ys83ibaaaaaaa
0123456789123
*************

Yeah brute-forcing this is gonna take too much time, I think I'm missing some info here