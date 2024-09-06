### Are you sure that's all?
![Question](https://github.com/alexbravo17/SecEduCTF2024Writeup/blob/main/Week1/images/areyousurethatsallq.png)

Got traffic.pcap

Opened in wireshark, there is a transfer from port 35122 to 12345, this is a PDF file since the header says %PDF

So, I followed the stream, chose conversation to be one way from 35122 -> 12345, change to show it as raw.
![wireshark pdf in binary](https://github.com/alexbravo17/SecEduCTF2024Writeup/blob/main/Week1/images/areyousurethatsall.png)

Saved it as a pdf file, then I got a pdf file with the flag **SECEDU{s0m3_empl0y33_b3n3fit5}**
