name = ['apples', 'bananas', 'oranges', 'cats', 'dogs']
verb = ['blue', 'green', 'red']
noun = ['261', '461', '669']
from random import randint
def pick(words):
    num_words = len(words)
    num_picked = randint(0, num_words - 1)
    word_picked = words[num_picked]
    return word_picked
while True:
     print(pick(verb), pick(name), pick(noun), end='.')
     print('Heres your username.')
     input()
