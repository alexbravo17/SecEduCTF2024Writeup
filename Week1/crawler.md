### Crawler

Given website http://chals.secedu.site:4999

wfuzz -c --hc 404 -w /usr/share/wordlists/wfuzz/general/common.txt -w /usr/share/wordlists/wfuzz/general/extensions_common.txt http://chals.secedu.site:4999/FUZZFUZ2Z

wfuzz -c --hc 404 -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-5000.txt -w /usr/share/wordlists/wfuzz/general/extensions_common.txt http://chals.secedu.site:4999/FUZZFUZ2Z

I give up, a teammate (thanks medley in UQ Cyber Squad!!!) found the file which is http://chals.secedu.site:4999/robots.txt

Quick look shows a bunch of .txt web files

curl http://chals.secedu.site:4999/robots.txt > textfiles
cat textfiles | awk '$1 == "Disallow:" {print $2}' | cut -c 2- > dict
This cleans textfiles into one where we can use for fuzzing again, then fuzz again

wfuzz -c --hc 404 -w dict -u http://chals.secedu.site:4999/FUZZ

SECEDU{th3r3_g0es_0ur_b3ndwidth}