### add_to_cartel
![Question](https://github.com/alexbravo17/SecEduCTF2024Writeup/blob/main/Week4/images/addtocartel.png)
Given a website http://chals.secedu.site:5016

Attempting to SQL injection and XSS doesnt seem to work
Looking at the source, there is a hidden form here with value=viewer
![BurpSuite form](https://github.com/alexbravo17/SecEduCTF2024Writeup/blob/main/Week4/images/addtocartel2.png)
Lets see what happens if we use BurpSuite to change it to member

Oh theres the flag
![Flag](https://github.com/alexbravo17/SecEduCTF2024Writeup/blob/main/Week4/images/addtocartel2.png)