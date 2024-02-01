import hashlib
import json

def hash_md5(input_string: str):
    # Convertir la chaîne en bytes
    input_bytes = input_string.encode()
    
    # Créer un objet hasher MD5
    md5_hasher = hashlib.md5()
    
    # Mettre à jour le hasher avec les bytes de la chaîne
    md5_hasher.update(input_bytes)
    
    # Récupérer le hash MD5 sous forme de chaîne hexadécimale
    md5_hash = md5_hasher.hexdigest()
    
    return md5_hash
data = {}
with open("dict-fr.txt", "r", encoding="utf-8") as f:
    for line in f.readlines():
        data[line.removesuffix("\n")] = hash_md5(line.removesuffix("\n"))
    
with open("md5.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)