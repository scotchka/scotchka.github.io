import random


def make_chain(raw_text):
    words = raw_text.split()

    chain = {}

    bigrams = list(zip(words[:-1], words[1:])) + [(words[-1], words[0])]

    for i, bigram in enumerate(bigrams):
        next_bigram = bigrams[(i + 1) % len(bigrams)]

        chain.setdefault(next_bigram, {})
        link = chain.setdefault(bigram, {})
        next_links = link.setdefault(bigram, [])
        next_links.append(chain[next_bigram])

    return chain


def make_text(chain):

    link = random.choice(list(chain.values()))

    text = ""

    while len(text) < 140:
        bigram = list(link.keys())[0]
        text = text + bigram[0] + " "
        link = random.choice(link[bigram])

    return text
