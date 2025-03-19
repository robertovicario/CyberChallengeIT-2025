# KERBEROS SIMULATOR

**1) Apro un autenticazione con il server, ricevo:**

Encrypted Key Message: `bDNzTVVsdEI4cm9PNjJFeXltU3V6ejlPTFV0bkxCakdBMTlpT0cySWRGVkU2bmFVa2h0RGs5U2I4UDI0TEZJYzJzVFZTUVFXbFEvMzdldzl0ZllYUmc9PQ==`
Authentication Ticket: `a3FrdVNxNTZweDFWK05rM290YXhES3pPZFp2TkdkaVNGLzk2SUJ0cm9wSkQrTS9MMWhrZjZXREdWdXdkdm1HcCtXOHkxQy95T29RcHBPWU54Tml5bVE9PQ==`


**2) Decifriamo Encrypted Message con la chiave '192883939', il server ritorna:**

`{K_A_TGS=873331, TGS=tgs1, Timestamp=2020:5:6:14:18:10}`


**3) Mandiamo al server l'autentication ticket ricevuto in precedenza nel punto (1):**


Authentication Ticket: `a3FrdVNxNTZweDFWK05rM290YXhES3pPZFp2TkdkaVNGLzk2SUJ0cm9wSkQrTS9MMWhrZjZXREdWdXdkdm1HcCtXOHkxQy95T29RcHBPWU54Tml5bVE9PQ==`

Mandando la flag solo ad Alice, autentichiamoci come lei: `{Alice, Timestamp=2020:5:6:14:18:10}`
Cifrandolo con la chiave '873331' ottenuta nel punto (2):
Ciphertext = `T0F5S3kxMG5YMFovY1ZzeEZBZnNiZ1o1THA4NEdybGg2TTUzVnp6K0NNeFRiaUNiQ0x4b3hOSUJnaWZSVzlHTQ==`
Mandiamo al server sia l'authentication ticket che il ciphertext.


**4) Il TGS risponde:**

Encrypted Message: `YXZyQ3pXUEFhbFo2OWZlY09PODhxUlJqYnRIUDBYdWVKYWxqYXJQQjdTTk1Dcnlra1BjSTlFNnY3cXA1cW9HRw==`
Decriptiamolo con la key ottenuta nel passo (2) -> Otteniamo `CCIT{K3rb3r0s_4uth3nt1c4t10n_Pr0t0c0l}`
