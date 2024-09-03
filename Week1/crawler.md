### Crawler

Given website http://chals.secedu.site:4999
![alt text](https://github.com/alexbravo17/SecEduCTF2024Writeup/tree/main/images/crawler1.png)

Let's try to web fuzz using `wfuzz`

```
wfuzz -c --hc 404 -w /usr/share/wordlists/wfuzz/general/common.txt -w /usr/share/wordlists/wfuzz/general/extensions_common.txt http://chals.secedu.site:4999/FUZZFUZ2Z

wfuzz -c --hc 404 -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-5000.txt -w /usr/share/wordlists/wfuzz/general/extensions_common.txt http://chals.secedu.site:4999/FUZZFUZ2Z
```

I give up, a teammate (thanks medley in UQ Cyber Squad!!!) found the file which is http://chals.secedu.site:4999/robots.txt

Quick look shows a bunch of .txt web files. Let's fuzz again to find which one gives status code 200

![alt text](https://github.com/alexbravo17/SecEduCTF2024Writeup/tree/main/images/crawler2.png)

Scrape, cut and clean the filenames to make a wordlist

```
curl http://chals.secedu.site:4999/robots.txt > textfiles
cat textfiles | awk '$1 == "Disallow:" {print $2}' | cut -c 2- > dict
wfuzz -c --hc 404 -w dict -u http://chals.secedu.site:4999/FUZZ
```

**SECEDU{th3r3_g0es_0ur_b3ndwidth}**