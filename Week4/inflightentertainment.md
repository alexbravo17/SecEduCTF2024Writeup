### in_flight_entertainment

Given a picture 
![Question](https://github.com/alexbravo17/SecEduCTF2024Writeup/blob/main/Week4/resources/pretty_landscape.jpg)
![Question](https://github.com/alexbravo17/SecEduCTF2024Writeup/blob/main/Week4/images/inflightentertainment.png)

We need to find the flight number
Already from picture, we know its a KLM plane, so Netherlands might be destination/arrival

using exiftools online, we know the approximate time and date, which is around 6 pm UTC+2 time, 20 October 2023
![exiftool result](https://github.com/alexbravo17/SecEduCTF2024Writeup/blob/main/Week4/images/inflightentertainment1.png)

Using online image location finder AI https://geospy.ai, the location is Zurich, which would make sense since question mentions international flight.
Zurich airport is an international airport
![AI location finder result](https://github.com/alexbravo17/SecEduCTF2024Writeup/blob/main/Week4/images/inflightentertainment4.png)

So, now we need to find a database that catalogues flights. I found one online which is https://www.flightera.net/en/

Now use search, KLM Royal Dutch Airways (Cityhopper is regional and doesn't include Zurich), first check flights from Zurich around that time. Tried KL1961 and KL1963 and it failed

![ZRH->AMS](https://github.com/alexbravo17/SecEduCTF2024Writeup/blob/main/Week4/images/inflightentertainment2.png)

So, try with Zurich as destination, tried KL1960 but didn't work, but **KL1962** worked!

![AMS->ZRH](https://github.com/alexbravo17/SecEduCTF2024Writeup/blob/main/Week4/images/inflightentertainment3.png)