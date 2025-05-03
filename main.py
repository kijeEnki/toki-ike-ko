import csv

original = input("Enter sentence: ")

def prepare():
    global table, punctuation, final
    punctuation, final = [",", "-", "–", "—", "'", '"', "“", "”", "‘", "’", ":", ";"], [".", "…", "...", "!", "!..", "…!", "?", "?..", "…?", "·", "•"]
    table = {}
    with open("korn.csv") as file:
        file = csv.reader(file)
        for line in file: table[line[0]] = ((line[2], line[4]), (line[1], line[3]))

def korn(text: str, ipa: bool = False):
    try: table; punctuation; final
    except NameError: prepare()
    sentence = []
    for mark in punctuation: text = text.replace(mark, "")
    ending = ""
    for mark in final:
        if text.endswith(mark): ending = mark; text = text.replace(mark, "")
    words, index = text.split(), 0
    for word in reversed(words):
        if word in table: sentence.append(table[word][ipa][index%2==0])
        else:
            if ipa: sentence.append(" ??? ")
            else: sentence.append(f"“{word}”")
        index += 1
    sentence = list(reversed(sentence))
    if not ipa: sentence.append(ending)
    return "".join(sentence)

print(korn(original))
print(f"/{korn(original, True)}/")