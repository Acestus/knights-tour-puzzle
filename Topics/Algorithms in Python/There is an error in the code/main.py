sentence = input()

def aver(sent):

    for sym in ['!', '?', ';', '.', '"', "'"]:
        sent = sent.replace(sym, '')

    words = sent.split()

    total = 0
    for word in words:
        total = total + len(word)

    if len(word) != 0:
        result = total
    else:
        result = 0

    return result / len(words)

print(aver(sentence))