### Fix 'n' find
![Question](https://github.com/alexbravo17/SecEduCTF2024Writeup/blob/main/Week1/images/fixnfindq.png)

Given files.zip

First of all, check if this is actually zip file `file files.zip`.
This is an actual zip file, so lets unzip it `unzip files.zip`.
![file](https://github.com/alexbravo17/SecEduCTF2024Writeup/blob/main/Week1/images/fixnfind1.png)

A lot of text files under random_files directory. Wondering if we just need to find it among these, so `cat * | grep SECEDU`

Got the flag **SECEDU{w04h!_th4t_w45_c0mpre55ing}**