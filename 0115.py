def check(text):
    result = True
    i = 0
    n = int(len(text) / 2)
    for i in range(n):
        if not text[i] == text[len(text) -1 - i]:
            result = False
    return result

