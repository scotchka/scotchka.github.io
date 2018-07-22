from random import choice


def markov(raw_text):
    words = raw_text.split()

    tokens = {}

    bigrams = list(zip(words[:-1], words[1:])) + [(words[-1], words[0])]

    for i, bigram in enumerate(bigrams):
        next_bigram = bigrams[(i + 1) % len(bigrams)]

        tokens.setdefault(next_bigram, {})
        tokens.setdefault(bigram, {}).setdefault(bigram, []).append(tokens[next_bigram])

    link = choice(list(tokens.values()))

    text = ""

    while len(text) < 140:
        bigram = list(link.keys())[0]
        text = text + bigram[0] + " "
        link = choice(link[bigram])

    return text
