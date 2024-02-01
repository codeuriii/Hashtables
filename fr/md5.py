import hashlib

def hash_md5(input_string):
    # Convertir la chaîne en bytes
    input_bytes = input_string.encode('utf-8')
    
    # Créer un objet hasher MD5
    md5_hasher = hashlib.md5()
    
    # Mettre à jour le hasher avec les bytes de la chaîne
    md5_hasher.update(input_bytes)
    
    # Récupérer le hash MD5 sous forme de chaîne hexadécimale
    md5_hash = md5_hasher.hexdigest()
    
    return md5_hash

