from string import digits, ascii_letters, punctuation

chars = list(digits + ascii_letters + punctuation)

def gen(reste: list[str]):
    data = []
    for element in reste:
        for char in chars:
            data.append(f"{element}{char}")
    return data

