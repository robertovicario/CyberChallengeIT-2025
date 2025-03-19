# KEY EXCHANGE

**1) Prendere chiave pubblica e privata di Alice.**
```
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCoSnsclIaWY4Mbp8arjQ8mp9zd
e6biFlrT7PEusLtbWAuLvYV97r2q4CwpS0sAsPbo91M1Jj/4KXDfb4UQ3oAZakyl
ASUNAbgV6+Tw3fX+PMf4hCgSN9eNskoKRexhxrt+JtfKHwu9CFeSYscV0RNS+3m9
Um3BWHrenw64eihZywIDAQAB
-----END PUBLIC KEY-----

-----BEGIN RSA PRIVATE KEY-----
MIICXQIBAAKBgQCoSnsclIaWY4Mbp8arjQ8mp9zde6biFlrT7PEusLtbWAuLvYV9
7r2q4CwpS0sAsPbo91M1Jj/4KXDfb4UQ3oAZakylASUNAbgV6+Tw3fX+PMf4hCgS
N9eNskoKRexhxrt+JtfKHwu9CFeSYscV0RNS+3m9Um3BWHrenw64eihZywIDAQAB
AoGBAKUOL8LvNTVIsm0sV2En/0UlfCzKOvohfMG/8Sie85L6PpC2t7e0sNdn+Egj
7ZLm/bOt5zEIq9LkKi0qfnL2FuG+vFNaBAkHNXnyyYKPVUVucbnUWJx2c/O8sxpp
wjZJD1esEaKDfiVk1/BNYaE8VNjFuMaW3dKwT8riVhNsr/u5AkEA2oXuWSF/61JG
9dwAyKfBHz/BtdQ53eHIISkX/U6Kj4BEMEK23WebrVPz96OWr1/llum7zCbcI6b2
Ko6mVXjx1QJBAMUnJdRrjYVIo1hElhXbHSu2zagikzv66q3/E5magcbFhmD7CBeb
wUeGcKW3pySDK/g+waFn5vpoHSFtkF2uTR8CQAx14J5ye5HWkjdIwT6v2iJHB2uv
21DcpAXICxclmF8QaFL8KuM7GjRq+hlf2aLMbBIL5+p/OMRLq/PHSJLNH7UCQEV7
Y4i2kvzLOc4s9dwkCebTGS3Naah06OqDgCvdWSltict6DUMMwJRtnBu7WuuyUve9
Xk59KNlNgh6612s8t68CQQC54eVLoso+W7vM/G9110SZvWtm2vC7maJbbz+6d3px
nV6mjxmR2638eKLgQLJGw3wFX3SqWYBYU0+kM1b2wOMl
-----END RSA PRIVATE KEY-----
```


**2) Ricuperiamo la chiave pubblica di Santa.**
Hello! This is Santa server!
My public key is:
```
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDh+G+5W2m6bQu5iAhiPsSS0YvJ
IPGNZ8JRhdZXSaqLnRw7I6eHc31XeC/9s9zzrSVDPrR33F13e2uTsdt8sYPusy3h
S6Zx9DPMOsi0+ZUmV0F10QAI//Kwm8NmbzLaS/sxYrA3scrPxwL8vyHwEXgo4spx
kK95AfPn2q723BoufQIDAQAB
-----END PUBLIC KEY-----
```


**3) Io (Alice) mando a Bob un messaggio 'Alice', concatenato con la mia chiave pubblica, S*Ks, Bob risponde:**
Hello Alice! This is Bob.

Encrypted Session Key:
`Q13gkTtqnHD7VM45Lzch0o5Npt9srnSXjXBsGY/5ofcIEjakkyOY0jhXwbOYO3jNfXLO4y6xhue35yOv4siD4x3IAg7w2Btd7FjGG2jal3kFC3S5Fkfo8RsF3QSNGVcOUM9t6nn1V8/j6jBNT4043IS4O4KKIw0ueueHFDu+q6c=`

Encrypted Credentials:
`dS9sbWozeWk4SnZuSElYQXFlbHU3UT09`


**3) Decifriamo 'Encrypted Session Key' con la mia chiave privata, essendo stato cifrato con la mia chiave pubblica ho il permesso di farlo ed ottengo:**
Plaintext: `tz8sTOsZTTXuMnZy` -> Chiave simmetrica.


**4) Con la chiave simmetrica trovata nel passo (3) decifro 'Encrypted Credentials' ed ottengo:**
Plaintext: `Bob Donner-2019` -> Significa che ho l'user con cui si autentica Bob.


**5) Cifro la chiave simmetrica del punto (3) con la chiave pubblica di Santa del punto (2), e concateno 'Encrypted Credentials' facendogli credere di essere Bob dalla sua credenziale e dal possesso della chiave simmetrica, dato che la flag viene mandata solo a lui, cosi ottengo:**
Reply: `U0hLZ3dQdVV6Q01iMzRQR1FoUGNnay9wL21BOEZwYmZRaEhrYnlTQm5Yamx3UHQxSTBWVjhNM3FsZHo3YmRzYQ==`
Decifro con la chiave simmetrica del punto (3) e ottengo -> `CCIT{C0ngr4tz_y0u_l34rn_k3y_3xch4ng3!}`
