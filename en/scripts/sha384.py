import hashlib
import json

def hash_md5(input_string: str):
    input_bytes = input_string.encode()
    
    md5_hasher = hashlib.sha384()
    
    md5_hasher.update(input_bytes)
    
    md5_hash = md5_hasher.hexdigest()
    
    return md5_hash
data = {}
with open("../dict-en.txt", "r", encoding="utf-8") as f:
    for line in f.readlines():
        data[line.removesuffix("\n")] = hash_md5(line.removesuffix("\n"))
    
with open("../result/sha384.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)