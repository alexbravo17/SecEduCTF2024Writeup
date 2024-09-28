### digital_doppelganger

Given website http://chals.secedu.site:5016 and image

![Question](https://github.com/alexbravo17/SecEduCTF2024Writeup/blob/main/Week4/images/digitaldoppelganger.png)
![Image in question](https://github.com/alexbravo17/SecEduCTF2024Writeup/blob/main/Week4/resources/IMG_8080.jpg)

We got a website that gives a percentage value of correct HTTP headers, so to BurpSuite to modify HTTP headers
![Website in question](https://github.com/alexbravo17/SecEduCTF2024Writeup/blob/main/Week4/images/digitaldoppelganger1.png)
![BurpSuite](https://github.com/alexbravo17/SecEduCTF2024Writeup/blob/main/Week4/images/digitaldoppelganger2.png)

So, check each header field to see if the value changes from 43%

Fields that needs to be updated:
- screenresolution 
- hardwareconcurrency
- timezone
- devicememory
- colordepth
- origin

Of these, origin is easy since the image shows a webpage http://super-secret-portal.corp
Colordepth I was lucky with and coincidentally got 32 as correct

So heres what I got so far
```
{
    "userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.112 Safari/537.36",
    "screenResolution":"1536x756",
    "colorDepth":32,
    "installedFonts":["Arial","Times New Roman","Helvetica"],
    "timezone":"America/New_York",
    "language":"en-US",
    "origin":"http://super-secret-portal.corp",
    "doNotTrack":"unspecified",
    "cookieEnabled":true,
    "hardwareConcurrency":8,
    "deviceMemory":"unknown"
}
```
Now, for the rest, the image shows a MacBook Air, exiftool shows that the image was taken on Nov 7 2022, which checks out with laptop's date. Using AI that can geolocates, it is in New York. Interestingly, the timezone is incorrect, but it should be correct with the location. Possibly due to Daylight Saving time maybe?

As for useragent, which is the main problem since the prompt says that its unauthorized browser, a lot of googling about user agents later, I come up with 
`"userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:10.0) Gecko/20100101 Firefox/10.0"`
Since, according to https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent/Firefox#macos, MacOS Firefox reporting is frozen at 10.15, and https://en.wikipedia.org/wiki/Firefox_version_history#Other_CPU_architectures says that Firefox version after 10 is discontinued? (unsure), but this does not work.

As for screenResolution, 2560x1664 is the length and width of Macbook Air M2, 2022 according to https://support.apple.com/en-us/111867, but this doesn't work. https://en.wikipedia.org/wiki/MacBook_Air_(Apple_silicon)#Technical_specifications_2 shows some supported scaled resolutions but all of them for 13" doesn't work.

At this point, I give up. Running out of ideas and very time-consuming.