import random
from Crypto.Util.number import bytes_to_long

def hash_collision(s):
    # Creiamo una lista di collisioni
    collisions = []
    
    while len(collisions) < 3:
        s2 = bytearray(s)
        
        # Modifichiamo una coppia di byte
        for i in range(0, len(s2) - 1, 2):
            original = bytes_to_long(s[i:i+2])
            modified = (original ^ random.randint(1, 255)).to_bytes(2, 'big')
            s2[i] = modified[0]
            s2[i+1] = modified[1]
            if bytes(s2) != s and bytes(s2) not in collisions:
                collisions.append(bytes(s2))
                break
    
    return collisions

# Testiamo con una stringa casuale
s = b"uk9Uqxpn9uGxWkJqvXJXpWmD2yugksia"
collisions = hash_collision(s)
for i, s2 in enumerate(collisions):
    print(f"Collision {i+1}: {s2}")
