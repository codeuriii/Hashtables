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
for i in range(4, 10):
    with open(f"lists/{i}.txt", "w") as f:
        for element in data:
            f.write(f"{element}\n")
    
    data = gen(data)