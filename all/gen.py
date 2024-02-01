from string import digits, ascii_letters, punctuation
import json

chars = list(digits + ascii_letters + punctuation)

def gen(reste: list[str]):
    data = []
    for element in reste:
        for char in chars:
            data.append(f"{element}{char}")
    return data

data = chars
for i in range(1, 10):
    with open(f"lists/{i}.json", "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
    data = gen(data)