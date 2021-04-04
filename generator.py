from random import randint
name = ['apples', 'bananas', 'oranges', 'cats', 'dogs']
verb = ['blue', 'green', 'red']
noun = [randint(1, 999)]
def pick(words):
    num_words = len(words)
    num_picked = randint(0, num_words - 1)
    word_picked = words[num_picked]
    return word_picked
while True:
     print(pick(verb), pick(name), pick(noun))
     print('Here\'s your username.')
     input()
    
